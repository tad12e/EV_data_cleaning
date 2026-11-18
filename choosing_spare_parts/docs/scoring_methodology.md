# Scoring Methodology for Import Priority Index

The **Import Priority Index (IPI)** is a composite metric designed to guide spare parts procurement:

$$\text{IPI} = 0.40(D) + 0.35(S) + 0.25(F)$$

Where:
* **$D$ (Demand Score, 40%)**:
  $$D = \text{Fleet Size Weight} \times \text{Daily Commuter Share}$$
* **$S$ (Scarcity Score, 35%)**:
  $$S = \left(1 - \frac{\text{Local Floor Stock Units}}{\text{Active Inquiries}}\right) \times 100$$
* **$F$ (Failure Severity Score, 25%)**:
  Evaluated on a scale of 0–100 where component failure renders the vehicle inoperable (e.g. OBC, Inverter = 90–95; suspension strut = 80; cosmetic body panel = 30).
