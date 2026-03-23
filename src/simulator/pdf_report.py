"""Professional PDF report generator for the Candor Simulator."""

import math
from pathlib import Path

from fpdf import FPDF

from .companies import get_all_companies
from .engine import score_company
from .models import RevealedScore, DecisionCategory


# ── Color Palette ───────────────────────────────────────────────────
DARK = (44, 62, 80)         # #2C3E50 — primary text
PEOPLE_GREEN = (46, 204, 113)  # #2ECC71
PROFIT_RED = (231, 76, 60)    # #E74C3C
AMBER = (243, 156, 18)        # #F39C12
LIGHT_BG = (236, 240, 241)    # #ECF0F1
WHITE = (255, 255, 255)
MEDIUM_GRAY = (149, 165, 166) # #95A5A6
DARK_GRAY = (127, 140, 141)   # #7F8C8D
NAVY = (26, 26, 46)           # #1A1A2E
ACCENT_BLUE = (52, 152, 219)  # #3498DB


def _ascii(text: str) -> str:
    """Replace unicode characters with ASCII equivalents for PDF core fonts."""
    return (
        text
        .replace("\u2014", " -- ")
        .replace("\u2013", "-")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2026", "...")
        .replace("\u2022", "*")
        .replace("\u25b2", "^")
    )


class CandorPDF(FPDF):
    """Professional PDF with Candor design system."""

    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="letter")
        self.set_auto_page_break(auto=True, margin=20)
        self._show_header = True

    def _safe_cell(self, w, h, txt="", **kwargs):
        super().cell(w, h, _ascii(str(txt)), **kwargs)

    def _safe_multi(self, w, h, txt="", **kwargs):
        super().multi_cell(w, h, _ascii(str(txt)), **kwargs)

    def header(self):
        if not self._show_header or self.page_no() == 1:
            return
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*MEDIUM_GRAY)
        self._safe_cell(0, 5, "CANDOR SIMULATOR", align="L")
        self.set_x(-60)
        self._safe_cell(50, 5, "The Revealed Compass of Corporate America", align="R")
        self.set_draw_color(*LIGHT_BG)
        self.line(self.l_margin, 12, self.w - self.r_margin, 12)
        self.ln(8)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-12)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*MEDIUM_GRAY)
        self._safe_cell(0, 5, f"{self.page_no()}", align="C")


def _score_color(profit_pct: float) -> tuple:
    """Gradient from green (people) to red (profit)."""
    if profit_pct <= 30:
        return PEOPLE_GREEN
    elif profit_pct <= 44:
        t = (profit_pct - 30) / 14
        return _lerp(PEOPLE_GREEN, AMBER, t)
    elif profit_pct <= 56:
        return AMBER
    elif profit_pct <= 70:
        t = (profit_pct - 56) / 14
        return _lerp(AMBER, PROFIT_RED, t)
    else:
        return PROFIT_RED


def _lerp(c1, c2, t):
    """Linear interpolation between two RGB tuples."""
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def generate_pdf(output_path: str = "candor_report.pdf") -> str:
    """Generate the professional PDF report."""
    companies = get_all_companies()
    scores = [score_company(c) for c in companies]
    scores.sort(key=lambda s: s.overall_profit_orientation)
    company_map = {c.ticker: c for c in companies}

    avg = sum(s.overall_profit_orientation for s in scores) / len(scores)
    median = scores[len(scores) // 2].overall_profit_orientation
    pos4_5 = sum(1 for s in scores if s.compass_position in (4, 5))
    pos1_2 = sum(1 for s in scores if s.compass_position in (1, 2))
    dead = sum(1 for s in scores if s.compass_position is None)

    pdf = CandorPDF()
    pdf.alias_nb_pages()

    # ═══════════════════════════════════════════════════════════
    # TITLE PAGE
    # ═══════════════════════════════════════════════════════════
    pdf.add_page()
    pdf._show_header = False

    # Dark banner at top
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, pdf.w, 105, "F")

    # Title text
    pdf.set_y(30)
    pdf.set_font("Helvetica", "B", 36)
    pdf.set_text_color(*WHITE)
    pdf._safe_cell(0, 14, "CANDOR", align="C")

    pdf.ln(14)
    pdf.set_font("Helvetica", "", 13)
    pdf.set_text_color(180, 190, 200)
    pdf._safe_cell(0, 7, "The Revealed Compass of Corporate America", align="C")

    pdf.ln(10)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(140, 150, 165)
    pdf._safe_cell(0, 6, f"{len(scores)} Companies Analyzed  |  Based on Public Record", align="C")

    # Compass graphic on title page
    pdf.set_y(115)
    _draw_compass_scale(pdf, pdf.w / 2, 132, 75, avg)

    # Stats boxes
    pdf.set_y(165)
    box_w = 42
    margin_between = 5
    total_w = box_w * 4 + margin_between * 3
    start_x = (pdf.w - total_w) / 2

    stat_boxes = [
        (f"{avg:.1f}%", "Average Score", DARK),
        (f"{pos1_2}", "People-Leaning", PEOPLE_GREEN),
        (f"{dead}", "Dead Zone", AMBER),
        (f"{pos4_5}", "Profit-Leaning", PROFIT_RED),
    ]

    boxes_y = pdf.get_y()
    for i, (value, label, color) in enumerate(stat_boxes):
        x = start_x + i * (box_w + margin_between)
        _draw_stat_box(pdf, x, boxes_y, box_w, 28, value, label, color)

    # Quote at bottom
    pdf.set_y(210)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(*DARK_GRAY)
    pdf._safe_multi(0, 5,
        '"It\'s not personal, it\'s business" is a sentence that\n'
        "has only ever been said by the person who gets to keep their job.",
        align="C")

    pdf.set_y(240)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*MEDIUM_GRAY)
    pdf._safe_cell(0, 5, "candor / noun / the quality of being open and honest in expression; frankness.", align="C")

    # ═══════════════════════════════════════════════════════════
    # METHODOLOGY
    # ═══════════════════════════════════════════════════════════
    pdf.add_page()
    pdf._show_header = True
    _section_header(pdf, "Methodology")

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*DARK)
    pdf._safe_multi(0, 5,
        "Each company is scored on publicly documented decisions across five "
        "weighted categories. All data is sourced from SEC filings, press releases, "
        "OSHA records, NLRB rulings, investigative reporting, and company statements.")
    pdf.ln(6)

    # Category weight bars
    categories = [
        ("Workforce Decisions", 30, "Layoffs, hiring, restructuring"),
        ("Compensation & Benefits", 25, "Pay, equity, healthcare, retirement"),
        ("Working Conditions & Safety", 20, "Work environment, safety, flexibility"),
        ("Communication & Transparency", 15, "How decisions are framed and delivered"),
        ("Investment in People", 10, "Training, development, career growth"),
    ]

    for name, weight, desc in categories:
        y = pdf.get_y()
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*DARK)
        pdf._safe_cell(90, 5, name)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*DARK_GRAY)
        pdf._safe_cell(20, 5, f"{weight}%")

        # Weight bar
        x = pdf.get_x() + 2
        bar_y = y + 1.5
        pdf.set_fill_color(*ACCENT_BLUE)
        pdf.rect(x, bar_y, weight * 1.5, 3, "F")
        pdf.ln(5)

        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*MEDIUM_GRAY)
        pdf._safe_cell(0, 4, f"    {desc}")
        pdf.ln(5)

    pdf.ln(4)

    # Compass position mapping
    _section_subheader(pdf, "Compass Position Mapping")
    positions = [
        ("0-29%", "Position 1", "People Primary", PEOPLE_GREEN),
        ("30-44%", "Position 2", "People Leaning", _lerp(PEOPLE_GREEN, AMBER, 0.5)),
        ("45-55%", "Dead Zone", "Pick a side", AMBER),
        ("56-70%", "Position 4", "Profit Leaning", _lerp(AMBER, PROFIT_RED, 0.5)),
        ("71-100%", "Position 5", "Profit Primary", PROFIT_RED),
    ]
    for range_str, pos_name, label, color in positions:
        pdf.set_fill_color(*color)
        pdf.rect(pdf.l_margin, pdf.get_y() + 1, 4, 4, "F")
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*DARK)
        pdf.set_x(pdf.l_margin + 7)
        pdf._safe_cell(22, 6, range_str)
        pdf._safe_cell(25, 6, pos_name)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*DARK_GRAY)
        pdf._safe_cell(50, 6, label)
        pdf.ln(7)

    pdf.ln(6)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(*MEDIUM_GRAY)
    pdf._safe_multi(0, 4,
        "Scores are interpretive. Reasonable people will disagree on individual numbers. "
        "The pattern is the point.")

    # ═══════════════════════════════════════════════════════════
    # DISTRIBUTION & SECTOR
    # ═══════════════════════════════════════════════════════════
    pdf.add_page()
    _section_header(pdf, "Distribution")

    dist_data = [
        ("Position 1 -- People Primary", sum(1 for s in scores if s.compass_position == 1), PEOPLE_GREEN),
        ("Position 2 -- People Leaning", sum(1 for s in scores if s.compass_position == 2), _lerp(PEOPLE_GREEN, AMBER, 0.5)),
        ("Dead Zone", sum(1 for s in scores if s.compass_position is None), AMBER),
        ("Position 4 -- Profit Leaning", sum(1 for s in scores if s.compass_position == 4), _lerp(AMBER, PROFIT_RED, 0.5)),
        ("Position 5 -- Profit Primary", sum(1 for s in scores if s.compass_position == 5), PROFIT_RED),
    ]

    max_count = max(d[1] for d in dist_data)
    for label, count, color in dist_data:
        pct = count / len(scores) * 100
        y = pdf.get_y()

        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*DARK)
        pdf._safe_cell(60, 7, label)

        bar_w = (count / max_count) * 80 if max_count > 0 else 0
        x = pdf.get_x() + 2
        pdf.set_fill_color(*color)
        pdf.rect(x, y + 1.5, bar_w, 4.5, "F")

        pdf.set_x(x + bar_w + 3)
        pdf.set_font("Helvetica", "B", 9)
        pdf._safe_cell(30, 7, f"{count}  ({pct:.0f}%)")
        pdf.ln(9)

    # Sector analysis
    pdf.ln(6)
    _section_header(pdf, "Sector Analysis")

    sectors = _sector_analysis(scores, companies)

    # Table header
    pdf.set_fill_color(*NAVY)
    y = pdf.get_y()
    pdf.rect(pdf.l_margin, y, pdf.w - pdf.l_margin - pdf.r_margin, 7, "F")
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*WHITE)
    pdf._safe_cell(55, 7, "  Sector")
    pdf._safe_cell(18, 7, "Score")
    pdf._safe_cell(35, 7, "")  # bar space
    pdf._safe_cell(22, 7, "Companies")
    pdf._safe_cell(30, 7, "Position")
    pdf.ln(7)

    for i, (sector, avg_score, count, position) in enumerate(sectors):
        y = pdf.get_y()
        if i % 2 == 0:
            pdf.set_fill_color(*LIGHT_BG)
            pdf.rect(pdf.l_margin, y, pdf.w - pdf.l_margin - pdf.r_margin, 7, "F")

        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*DARK)
        pdf._safe_cell(55, 7, f"  {sector}")
        pdf._safe_cell(18, 7, f"{avg_score:.1f}%")

        # Score bar
        bar_x = pdf.get_x() + 2
        bar_w = avg_score / 100 * 30
        color = _score_color(avg_score)
        pdf.set_fill_color(*color)
        pdf.rect(bar_x, y + 2, bar_w, 3, "F")
        pdf._safe_cell(35, 7, "")

        pdf._safe_cell(22, 7, f"{count}")
        pdf.set_text_color(*DARK_GRAY)
        pdf._safe_cell(30, 7, position)
        pdf.ln(7)

    # ═══════════════════════════════════════════════════════════
    # RANKED LIST
    # ═══════════════════════════════════════════════════════════
    pdf.add_page()
    _section_header(pdf, "Complete Rankings")
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*DARK_GRAY)
    pdf._safe_cell(0, 5, "Ranked from most people-oriented to most profit-oriented")
    pdf.ln(6)

    _draw_ranking_table(pdf, scores, company_map)

    # ═══════════════════════════════════════════════════════════
    # OBSERVATIONS
    # ═══════════════════════════════════════════════════════════
    pdf.add_page()
    _section_header(pdf, "Observations")

    observations = [
        ("Corporate America leans profit.",
         f"The average score across {len(scores)} companies is {avg:.1f}% "
         f"profit-oriented. The median is {median:.1f}%. Neither is in "
         f"people-first territory."),

        ("The compass tilts one direction.",
         f"{pos4_5} companies land at Position 4 or 5 (profit-leaning or primary). "
         f"{pos1_2} land at Position 1 or 2 (people-leaning or primary). "
         f"The ratio is {pos4_5/max(pos1_2,1):.1f} to 1."),

        ("No sector averages below Position 2.",
         "People-first orientation is the exception at every level of the economy, "
         "not the rule. Even the most people-friendly sectors hover near the dead zone."),

        ("Growth makes generosity easy.",
         "The most people-oriented companies -- Costco, NVIDIA, AMD, Eli Lilly -- share "
         "a common trait: they're growing. It's easy to invest in people when revenue "
         "is rising. The real test comes when it stops."),

        ("Gravity doesn't accept euphemisms.",
         "Boeing scores highest in conditions -- not because it's the worst employer, "
         "but because people died. Most companies extract value from employees quietly. "
         "Boeing's extraction became visible because physics doesn't have a PR department."),

        ("The revealed compass doesn't lie.",
         f"Every company on this list has said 'our people are our greatest asset.' "
         f"The average score is {avg:.1f}% profit-oriented. Most companies have "
         f"already picked a side. They just haven't said it out loud."),
    ]

    for i, (title, body) in enumerate(observations, 1):
        y = pdf.get_y()
        if pdf.get_y() > 235:
            pdf.add_page()

        # Number circle
        pdf.set_fill_color(*NAVY)
        cx = pdf.l_margin + 4
        cy = y + 3
        pdf.ellipse(cx - 3.5, cy - 3.5, 7, 7, "F")
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_text_color(*WHITE)
        pdf.set_xy(cx - 3.5, cy - 2.5)
        pdf._safe_cell(7, 5, str(i), align="C")

        # Title and body
        pdf.set_xy(pdf.l_margin + 14, y)
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*DARK)
        pdf._safe_cell(0, 6, title)
        pdf.ln(6)

        pdf.set_x(pdf.l_margin + 14)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*DARK_GRAY)
        pdf._safe_multi(pdf.w - pdf.l_margin - pdf.r_margin - 14, 5, body)
        pdf.ln(6)

    # ═══════════════════════════════════════════════════════════
    # COMPANY DETAILS
    # ═══════════════════════════════════════════════════════════
    pdf.add_page()
    _section_header(pdf, "Company Profiles")
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*DARK_GRAY)
    pdf._safe_cell(0, 5, "Category breakdown for each company")
    pdf.ln(8)

    cat_labels = {
        DecisionCategory.WORKFORCE: "Workforce",
        DecisionCategory.COMPENSATION: "Compensation",
        DecisionCategory.CONDITIONS: "Conditions",
        DecisionCategory.COMMUNICATION: "Communication",
        DecisionCategory.INVESTMENT: "Investment",
    }

    for idx, s in enumerate(scores):
        # Estimate height: header(5) + subheader(5) + categories(n*3.5) + padding(8)
        n_cats = len(s.category_scores)
        profile_h = 5 + 5 + n_cats * 3.5 + 8
        if pdf.get_y() + profile_h > pdf.h - 25:
            pdf.add_page()

        company = company_map.get(s.ticker)
        sector = company.sector if company else ""
        pos_str = (
            f"Position {s.compass_position} ({s.compass_label})"
            if s.compass_position else s.compass_label
        )

        y = pdf.get_y()

        # Company header bar
        color = _score_color(s.overall_profit_orientation)
        pdf.set_fill_color(*color)
        pdf.rect(pdf.l_margin, y, 3, 14, "F")

        pdf.set_x(pdf.l_margin + 5)
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*DARK)
        pdf._safe_cell(60, 5, f"{s.company} ({s.ticker})")
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*DARK_GRAY)
        pdf._safe_cell(0, 5, sector)
        pdf.ln(5)

        pdf.set_x(pdf.l_margin + 5)
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*MEDIUM_GRAY)
        pdf._safe_cell(0, 4,
            f"{s.overall_profit_orientation:.1f}% profit  |  {pos_str}  |  "
            f"{s.total_decisions} decisions  |  {s.period}")
        pdf.ln(5)

        # Category mini-bars
        pdf.set_x(pdf.l_margin + 5)
        for cs in s.category_scores:
            label = cat_labels.get(cs.category, str(cs.category))
            cat_color = _score_color(cs.profit_orientation)

            pdf.set_font("Helvetica", "", 7)
            pdf.set_text_color(*DARK)
            pdf.set_x(pdf.l_margin + 5)
            pdf._safe_cell(22, 3.5, label)

            bx = pdf.get_x()
            by = pdf.get_y() + 0.5
            pdf.set_fill_color(230, 230, 230)
            pdf.rect(bx, by, 30, 2.5, "F")
            pdf.set_fill_color(*cat_color)
            pdf.rect(bx, by, cs.profit_orientation / 100 * 30, 2.5, "F")

            pdf.set_x(bx + 32)
            pdf.set_text_color(*DARK_GRAY)
            pdf._safe_cell(15, 3.5, f"{cs.profit_orientation:.0f}%")
            pdf.ln(3.5)

        pdf.ln(5)

    # ═══════════════════════════════════════════════════════════
    # CLOSING PAGE
    # ═══════════════════════════════════════════════════════════
    pdf.add_page()

    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, pdf.w, pdf.h, "F")

    pdf.set_y(60)
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(*WHITE)
    pdf._safe_cell(0, 12, "CANDOR", align="C")

    pdf.ln(20)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(180, 190, 200)
    pdf._safe_multi(0, 6,
        "Scores are interpretive. Reasonable people will disagree\n"
        "on individual numbers. The pattern is the point.",
        align="C")

    pdf.ln(12)
    pdf._safe_multi(0, 6,
        "Every company on this list can choose any position on the\n"
        "compass. There is nothing inherently wrong with any position.\n"
        "What matters is being honest about what that position means.",
        align="C")

    pdf.ln(12)
    pdf._safe_multi(0, 6,
        "If you're 100% either way, you don't need this system.\n"
        "Candor exists for the space where both things matter and\n"
        "you need help navigating the tension honestly.",
        align="C")

    pdf.ln(30)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(100, 110, 130)
    pdf._safe_cell(0, 5, "github.com/DendroLabs/candor", align="C")

    # Save
    pdf.output(output_path)
    return output_path


# ── Drawing Helpers ─────────────────────────────────────────────────

def _section_header(pdf: CandorPDF, title: str):
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(*DARK)
    pdf._safe_cell(0, 8, title)
    pdf.ln(10)
    pdf.set_draw_color(*NAVY)
    pdf.set_line_width(0.8)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.l_margin + 40, pdf.get_y())
    pdf.set_line_width(0.2)
    pdf.ln(4)


def _section_subheader(pdf: CandorPDF, title: str):
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*DARK)
    pdf._safe_cell(0, 6, title)
    pdf.ln(5)


def _draw_stat_box(pdf, x, y, w, h, value, label, color):
    """Draw a statistics box with colored top border."""
    # Box background
    pdf.set_fill_color(*WHITE)
    pdf.rect(x, y, w, h, "F")

    # Colored top border
    pdf.set_fill_color(*color)
    pdf.rect(x, y, w, 2, "F")

    # Subtle border
    pdf.set_draw_color(*LIGHT_BG)
    pdf.rect(x, y, w, h, "D")

    # Value
    pdf.set_xy(x, y + 5)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(*DARK)
    pdf._safe_cell(w, 10, value, align="C")

    # Label
    pdf.set_xy(x, y + 17)
    pdf.set_font("Helvetica", "", 7)
    pdf.set_text_color(*DARK_GRAY)
    pdf._safe_cell(w, 5, label, align="C")


def _draw_compass_scale(pdf, cx, cy, width, marker_pct):
    """Draw the compass scale visualization."""
    half = width / 2
    left = cx - half
    right = cx + half

    # Background track
    pdf.set_fill_color(*LIGHT_BG)
    pdf.rect(left, cy - 2, width, 4, "F")

    # Gradient fill
    segments = 50
    seg_w = width / segments
    for i in range(segments):
        pct = i / segments * 100
        color = _score_color(pct)
        pdf.set_fill_color(*color)
        pdf.rect(left + i * seg_w, cy - 2, seg_w + 0.5, 4, "F")

    # Position markers
    positions = [
        (15, "1", "People\nPrimary"),
        (37, "2", "People\nLeaning"),
        (50, "X", "Dead\nZone"),
        (63, "4", "Profit\nLeaning"),
        (85, "5", "Profit\nPrimary"),
    ]

    for pct, num, label in positions:
        x = left + (pct / 100 * width)
        # Tick mark
        pdf.set_draw_color(*DARK)
        pdf.line(x, cy - 4, x, cy + 4)

        # Number
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_text_color(*DARK)
        pdf.set_xy(x - 4, cy + 5)
        pdf._safe_cell(8, 4, num, align="C")

        # Label
        pdf.set_font("Helvetica", "", 6)
        pdf.set_text_color(*MEDIUM_GRAY)
        pdf.set_xy(x - 10, cy + 9)
        pdf._safe_multi(20, 3, label, align="C")

    # Average marker (triangle)
    marker_x = left + (marker_pct / 100 * width)
    pdf.set_fill_color(*NAVY)
    # Draw triangle pointing down
    size = 3
    pdf.polygon([
        (marker_x - size, cy - 5),
        (marker_x + size, cy - 5),
        (marker_x, cy - 2),
    ], style="F")

    # Label for marker
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_text_color(*NAVY)
    pdf.set_xy(marker_x - 15, cy - 11)
    pdf._safe_cell(30, 4, f"AVG {marker_pct:.1f}%", align="C")

    # PEOPLE / PROFIT labels
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*PEOPLE_GREEN)
    pdf.set_xy(left - 2, cy - 8)
    pdf._safe_cell(20, 4, "PEOPLE")
    pdf.set_text_color(*PROFIT_RED)
    pdf.set_xy(right - 18, cy - 8)
    pdf._safe_cell(20, 4, "PROFIT")


def _draw_ranking_table(pdf, scores, company_map):
    """Draw the full ranked table with color bars."""
    page_w = pdf.w - pdf.l_margin - pdf.r_margin

    def _table_header():
        y = pdf.get_y()
        pdf.set_fill_color(*NAVY)
        pdf.rect(pdf.l_margin, y, page_w, 6, "F")
        pdf.set_font("Helvetica", "B", 7)
        pdf.set_text_color(*WHITE)
        pdf._safe_cell(8, 6, "  #")
        pdf._safe_cell(50, 6, "Company")
        pdf._safe_cell(14, 6, "Score")
        pdf._safe_cell(32, 6, "")
        pdf._safe_cell(30, 6, "Position")
        pdf._safe_cell(40, 6, "Sector")
        pdf.ln(7)

    _table_header()

    for i, s in enumerate(scores, 1):
        if pdf.get_y() > 248:
            pdf.add_page()
            _table_header()

        y = pdf.get_y()
        row_h = 5.5

        # Alternating row background
        if i % 2 == 0:
            pdf.set_fill_color(248, 249, 250)
            pdf.rect(pdf.l_margin, y, page_w, row_h, "F")

        company = company_map.get(s.ticker)
        sector = company.sector if company else ""
        pos_str = f"Pos {s.compass_position}" if s.compass_position else "Dead Zone"

        pdf.set_font("Helvetica", "", 7)
        pdf.set_text_color(*DARK)
        pdf._safe_cell(8, row_h, f"  {i}")
        pdf.set_font("Helvetica", "B", 7)
        pdf._safe_cell(50, row_h, f"{s.company} ({s.ticker})")
        pdf.set_font("Helvetica", "", 7)
        pdf._safe_cell(14, row_h, f"{s.overall_profit_orientation:.1f}%")

        # Color bar
        bx = pdf.get_x() + 1
        by = y + 1.5
        bar_full = 28
        bar_filled = s.overall_profit_orientation / 100 * bar_full
        color = _score_color(s.overall_profit_orientation)

        pdf.set_fill_color(230, 230, 230)
        pdf.rect(bx, by, bar_full, 2.5, "F")
        pdf.set_fill_color(*color)
        pdf.rect(bx, by, bar_filled, 2.5, "F")
        pdf._safe_cell(32, row_h, "")

        pdf.set_text_color(*DARK_GRAY)
        pdf._safe_cell(30, row_h, pos_str)
        pdf.set_font("Helvetica", "", 6.5)
        pdf._safe_cell(40, row_h, sector[:28])
        pdf.ln(row_h)


def _sector_analysis(scores, companies):
    from collections import defaultdict
    sector_scores = defaultdict(list)
    for s in scores:
        for c in companies:
            if c.ticker == s.ticker:
                sector = c.sector.split("/")[0].strip()
                sector_scores[sector].append(s.overall_profit_orientation)
                break

    result = []
    for sector, vals in sorted(sector_scores.items(), key=lambda x: sum(x[1]) / len(x[1])):
        avg = sum(vals) / len(vals)
        if avg <= 29: pos = "Position 1"
        elif avg <= 44: pos = "Position 2"
        elif avg <= 55: pos = "Dead Zone"
        elif avg <= 70: pos = "Position 4"
        else: pos = "Position 5"
        result.append((sector, avg, len(vals), pos))
    return result
