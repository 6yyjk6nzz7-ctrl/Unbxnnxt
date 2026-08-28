"""Compact inline-SVG QR codes (no external files, no <img>)."""
import qrcode


def qr_svg(data, size_mm=17, fg="#100D0F", bg=None, quiet=2):
    """Return an <svg> string drawing `data` as a QR code, sized in mm."""
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, border=0)
    q.add_data(data)
    q.make(fit=True)
    m = q.get_matrix()
    n = len(m)
    total = n + quiet * 2

    # Merge horizontal runs, then emit ONE <path> with many subpaths.
    # A rect-per-module SVG makes Chromium's PDF vector export pathologically
    # slow (thousands of elements per code); a single path renders instantly.
    seg = []
    for y, row in enumerate(m):
        x = 0
        while x < n:
            if row[x]:
                run = 1
                while x + run < n and row[x + run]:
                    run += 1
                seg.append(f"M{x + quiet} {y + quiet}h{run}v1h-{run}z")
                x += run
            else:
                x += 1

    bg_rect = f'<rect width="{total}" height="{total}" fill="{bg}"/>' if bg else ""
    return (
        f'<svg class="qr" viewBox="0 0 {total} {total}" width="{size_mm}mm" height="{size_mm}mm" '
        f'shape-rendering="crispEdges" xmlns="http://www.w3.org/2000/svg">'
        f'{bg_rect}<path fill="{fg}" d="{"".join(seg)}"/></svg>'
    )


if __name__ == "__main__":
    s = qr_svg("https://docs.claude.com/en/docs/claude-code/overview")
    print(len(s), "bytes")
    print(s[:200])
