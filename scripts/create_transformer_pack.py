from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist/materials/transformers-starter.pdf'
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
INK=HexColor('#173b36'); GRAY=HexColor('#54615d'); CREAM=HexColor('#faf8f2')
c=canvas.Canvas(str(OUT),pagesize=(595,842))
c.setTitle('Transformers - Concept Starter | JE Notes')
c.setAuthor('JE Notes')
style=ParagraphStyle('body',fontName='DejaVu',fontSize=10.2,leading=16,textColor=INK)
def p(t,y,width=483):
 x=Paragraph(t,style); w,h=x.wrap(width,1000); x.drawOn(c,56,y-h); return y-h-12
def head(n,title,sub):
 c.setFillColor(CREAM); c.rect(0,0,595,842,fill=1,stroke=0)
 c.setFillColor(INK); c.setFont('DejaVuBold',11); c.drawString(56,795,'JE NOTES / ELECTRICAL')
 c.setStrokeColor(HexColor('#d4ddd6')); c.line(56,778,539,778)
 c.setFont('DejaVuBold',24); c.drawString(56,731,title)
 p(sub,709)
 c.setFont('DejaVu',8); c.setFillColor(GRAY)
 c.drawString(56,37,'Original concept starter • 14 October 2026 • Not an official exam publication')
 c.drawRightString(539,37,f'{n} / 4')
def label(t,y):
 c.setFillColor(INK); c.setFont('DejaVuBold',12); c.drawString(56,y,t); return y-13
def formula(t,y):
 c.setFillColor(HexColor('#e7eee6')); c.roundRect(56,y-43,483,46,7,fill=1,stroke=0)
 c.setFillColor(INK); c.setFont('DejaVuBold',13); c.drawString(73,y-25,t); return y-61
head(1,'Transformers, made clear.','A focused starter for electrical fundamentals used in SSC JE and RRB JE preparation. This is not a complete transformer chapter or syllabus guide.')
y=label('01 / What fixes the core flux?',650)
y=p('An alternating core flux induces an emf in each winding. For sinusoidal flux with maximum value Φ<sub>m</sub>, the RMS induced emf is:',y)
y=formula('E = 4.44 f N Φm',y)
y=p('Here E is in volts, f in hertz, N is the number of turns, and Φ<sub>m</sub> in webers. The factor 4.44 assumes sinusoidal flux. With a small primary impedance drop, V<sub>1</sub> ≈ E<sub>1</sub>, so flux is approximately proportional to V<sub>1</sub>/f.',y)
y=label('02 / Ideal turns, voltage and current ratios',y-6)
y=formula('a = N1/N2 = V1/V2 = I2/I1',y)
y=p('These are magnitude relations for an ideal transformer under load. Input power equals output power. Real transformers have winding losses, core losses, leakage flux and a nonzero excitation current.',y)
y=label('03 / The no-load current has two components',y-6)
y=p('In the usual approximate model, I<sub>c</sub> is in phase with supply voltage and supplies core loss. I<sub>m</sub> is approximately 90° behind voltage and establishes flux. Thus I<sub>0</sub> = √(I<sub>c</sub>² + I<sub>m</sub>²), not I<sub>c</sub> + I<sub>m</sub>.',y)
y=p('When load increases at fixed voltage and frequency, the primary draws an additional load component. It largely balances the secondary ampere-turns; it does not mean that core flux rises in proportion to load.',y)
c.showPage()
head(2,'When conditions change.','Use the assumptions before using the formula. These comparisons assume the same winding turns.')
y=652
rows=[('Voltage decreases; frequency fixed','Core flux decreases approximately with voltage. In the normal unsaturated operating region, magnetising current generally decreases. It does not rise to restore the old flux.'),('Frequency decreases; voltage fixed','Core flux increases approximately as 1/f. Saturation and a large excitation current can result. Do not assume magnetising current is linear with flux near saturation.'),('Voltage and frequency decrease together','If V/f is held constant, core flux is approximately constant while winding drops are small. At very low frequency, winding resistance makes the approximation less accurate.'),('Load increases; voltage and frequency fixed','Primary load current increases. Core flux stays approximately constant. Copper loss increases approximately with the square of load current at fixed resistance.'),('Power factor decreases; kVA fixed','Current is unchanged at fixed voltage, so copper loss is approximately unchanged. Real output power decreases. Do not confuse fixed kVA with fixed kW.')]
for title,body in rows:
 y=label(title,y); y=p(body,y)-13
c.showPage()
head(3,'Solve it without a calculator.','Three original worked examples. These are practice models, not actual previous-year questions.')
y=label('01 / Voltage, frequency and flux',652)
y=p('A transformer operates at 200 V and 50 Hz. The supply changes to 180 V and 45 Hz. Neglect primary winding drops. Find the new-to-old maximum flux ratio.',y)
y=formula('Φnew/Φold = (180/200) × (50/45) = 1',y)
y=p('Both voltage and frequency fall by 10%. Their ratio is unchanged, so the maximum flux is approximately unchanged.',y)
y=label('02 / No-load current',y-7)
y=p('The core-loss component is 0.6 A and the magnetising component is 0.8 A. Assume these components are perpendicular. Find no-load current and no-load power factor.',y)
y=formula('I0 = √(0.6² + 0.8²) = 1 A; pf = 0.6',y)
y=p('Recognise the 3-4-5 triangle scaled by 0.2. The power factor is I<sub>c</sub>/I<sub>0</sub>, and is lagging in this model.',y)
y=label('03 / Load for maximum efficiency',y-7)
y=p('Core loss is 100 W and full-load copper loss is 400 W. At fixed voltage, frequency, resistance and load power factor, find the fraction x of full load for maximum efficiency.',y)
y=formula('x² × 400 = 100  →  x = 1/2',y)
y=p('Maximum efficiency occurs when variable copper loss equals approximately constant core loss. The answer is half load, not one-quarter load. This is ordinary efficiency, not all-day energy efficiency.',y)
c.showPage()
head(4,'Try it. Then check it.','Six original practice questions with short solutions. Cover the answer section while attempting them.')
y=651
qs=['1. An ideal transformer has N₁/N₂ = 5. Its primary voltage is 230 V. What is its secondary voltage?', '2. For that ideal transformer, secondary load current is 10 A. What is primary current?', '3. At fixed frequency, applied voltage falls by 20%. Neglect winding drops. How does maximum flux change?', '4. At constant winding resistance, load current is halved. What fraction of the original copper loss remains?', '5. I₀ = 5 A and I꜀ = 3 A in the approximate no-load model. Find Iₘ.', '6. Core loss is 200 W and full-load copper loss is 800 W. At what load fraction is ordinary efficiency maximum under the usual constant-loss assumptions?']
for q in qs: y=p(q,y)-4
y=label('Answers and reasoning',y-7)
for ans in ['1. 46 V. V₂ = 230/5.', '2. 2 A. I₁ = I₂/a = 10/5.', '3. It falls by approximately 20%, since Φₘ ∝ V/f.', '4. One-quarter. Copper loss ∝ I².', '5. 4 A. Iₘ = √(5² − 3²).', '6. Half load. x = √(200/800) = 1/2.']:
 y=p(ans,y)
p('Next topics to study: equivalent circuit, open-circuit and short-circuit tests, regulation, losses, efficiency, autotransformers and parallel operation.',max(y-4,85))
c.save()
print(OUT)
