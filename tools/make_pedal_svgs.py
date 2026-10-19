"""Draws the four planned Linework pedals in the same style as img/flashover.svg.

Run from the repo root: python tools/make_pedal_svgs.py
The controls are placeholders until each pedal is designed."""
import math, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img")


def ring(cx, cy, r, dot, lit, on, off):
    # 11 LEDs, 30 degrees apart, from 7 o'clock to 5 o'clock
    out = []
    for i in range(11):
        a = math.radians(-150 + 30 * i)
        x, y = cx + r * math.sin(a), cy - r * math.cos(a)
        out.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>' % (x, y, dot, on if (i + 1) in lit else off))
    return ''.join(out)


def knob(cx, cy, lit, c, big=False):
    r_ring, r_knob, r_base, dot = (32, 21, 38, 2.4) if big else (20, 14, 25, 1.9)
    return ('    <g>\n'
            '      <circle cx="%s" cy="%s" r="%s" fill="%s" fill-opacity="0.55"/>\n'
            '      <g>%s</g>\n'
            '      <circle cx="%s" cy="%s" r="%s" fill="url(#knob)"/>\n'
            '    </g>\n') % (cx, cy, r_base, c['dark'], ring(cx, cy, r_ring, dot, lit, c['lit'], c['dark']), cx, cy, r_knob)


def led(x, y, color, lit=True, r=3.5):
    if not lit:
        return '  <circle cx="%s" cy="%s" r="%s" fill="%s"/>\n' % (x, y, r, '#00000055')
    return ('  <circle cx="%s" cy="%s" r="%s" fill="%s"/>\n'
            '  <circle cx="%s" cy="%s" r="%s" fill="%s" fill-opacity="0.25"/>\n') % (x, y, r, color, x, y, r * 2.2, color)


def label(x, y, text, c, size=9):
    return '  <text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="middle" letter-spacing="1">%s</text>\n' % (x, y, size, c['text'], text)


def pedal(slug, title, words, c, controls, middle):
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 300" width="200" height="300" font-family="Arial, Helvetica, sans-serif">\n',
         '  <title>%s (illustration)</title>\n' % title,
         '  <defs>\n'
         '    <linearGradient id="body" x1="0" y1="0" x2="0" y2="1">\n'
         '      <stop offset="0" stop-color="%s"/>\n'
         '      <stop offset="1" stop-color="%s"/>\n'
         '    </linearGradient>\n'
         '    <radialGradient id="knob" cx="0.4" cy="0.35" r="0.7">\n'
         '      <stop offset="0" stop-color="#4a4f55"/>\n'
         '      <stop offset="1" stop-color="#1b1d20"/>\n'
         '    </radialGradient>\n'
         '  </defs>\n' % (c['top'], c['bottom']),
         '  <rect x="6" y="6" width="188" height="288" rx="16" fill="url(#body)" stroke="%s" stroke-width="2"/>\n\n' % c['edge'],
         '  <!-- Endless knobs with 11-LED rings -->\n']
    s += controls
    s.append('\n')
    s += middle
    s.append('\n  <!-- Name -->\n')
    for i, w in enumerate(words):
        s.append('  <text x="100" y="%d" font-size="17" font-weight="700" fill="#ffffff" fill-opacity="0.95" text-anchor="middle" letter-spacing="2.5">%s</text>\n' % (180 + 19 * i, w))
    s.append('  <text x="100" y="%d" font-size="7.5" fill="%s" text-anchor="middle" letter-spacing="2.5">GREYWIRE · LINEWORK</text>\n\n' % (180 + 19 * len(words) - 4, c['text']))
    s.append('  <!-- On LED, Link LED and footswitch -->\n')
    s.append(led(100, 230, c['on']))
    s.append(led(160, 230, '#7fd0ff', r=3))
    s.append(label(160, 246, 'LINK', c, 7))
    s.append('  <circle cx="100" cy="264" r="20" fill="#b7bcc2" stroke="#6b7076" stroke-width="2"/>\n'
             '  <circle cx="100" cy="264" r="13" fill="#d7dbe0" stroke="#8a8f95"/>\n'
             '</svg>\n')
    open('%s/%s.svg' % (OUT, slug), 'w', encoding='utf-8', newline='\n').write(''.join(s))


def three_knobs(c, names, lits):
    out = [knob(x, 64, lit, c) for x, lit in zip((48, 100, 152), lits)]
    out += [label(x, 104, n, c, 9 if len(n) < 7 else 7.5) for x, n in zip((48, 100, 152), names)]
    return out


def tempo_led(c):
    return ['  <!-- Tempo LED: blinks with the song tempo -->\n', led(100, 130, c['on'], r=3), label(100, 148, 'TEMPO', c, 8)]


# Tap Changer: clean boost, one large Level knob
c = dict(top='#3f8a63', bottom='#24563c', edge='#173a28', dark='#173a28', lit='#d6f5e2', text='#d9f0e2', on='#ff6a3d')
pedal('tap-changer', 'Tap Changer clean boost', ['TAP', 'CHANGER'], c,
      [knob(100, 76, range(1, 9), c, big=True), label(100, 134, 'LEVEL', c)], [])

# Three Phase: phaser
c = dict(top='#6d4fa6', bottom='#432e6b', edge='#2a1c45', dark='#2a1c45', lit='#e6dcff', text='#e3dbf5', on='#ff6a3d')
pedal('three-phase', 'Three Phase phaser', ['THREE', 'PHASE'], c,
      three_knobs(c, ('RATE', 'DEPTH', 'FEEDBACK'), (range(1, 5), range(1, 9), range(1, 6))), tempo_led(c))

# Rolling Blackout: tremolo, dark with amber
c = dict(top='#3a3b3f', bottom='#202124', edge='#111214', dark='#111214', lit='#ffc95e', text='#f1d9a6', on='#ffb03a')
pedal('rolling-blackout', 'Rolling Blackout tremolo', ['ROLLING', 'BLACKOUT'], c,
      three_knobs(c, ('RATE', 'DEPTH', 'SHAPE'), (range(1, 7), range(1, 10), {4})), tempo_led(c))

# Double Circuit: chorus with a Chorus/Vibrato button
c = dict(top='#2a8790', bottom='#185158', edge='#0d3338', dark='#0d3338', lit='#d4fbff', text='#d3eef1', on='#ff6a3d')
middle = ['  <!-- Chorus / Vibrato button with its two LEDs -->\n',
          led(68, 132, '#9ff3ff'), led(132, 132, '#9ff3ff', lit=False),
          '  <rect x="88" y="123" width="24" height="18" rx="4" fill="#26292d" stroke="%s"/>\n' % c['edge'],
          label(68, 152, 'CHORUS', c, 8), label(132, 152, 'VIBRATO', c, 8)]
pedal('double-circuit', 'Double Circuit chorus', ['DOUBLE', 'CIRCUIT'], c,
      three_knobs(c, ('RATE', 'DEPTH', 'MIX'), (range(1, 4), range(1, 7), range(1, 6))), middle)
