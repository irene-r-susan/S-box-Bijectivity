# Cellular Automata S-Box Verification (Class 1,3,1)

A small, dependency-free Python script that independently verifies the cryptographic
claims made about the **Class (1,3,1)** 4×4 S-box construction used in
*"Lightweight and Side-Channel Secure 4×4 S-Boxes from Cellular Automata Rules."*

The S-box is built from a single 4-variable Boolean function, evaluated four times
over cyclically shifted inputs to produce the full 4-bit output. This script
exhaustively checks all 16 possible inputs and confirms:

- **Bijectivity** — every input maps to a unique output (a true 1-to-1 permutation)
- **Differential Branch Number** — the worst-case diffusion score across all input/output pairs

## Background

An S-box (substitution box) is the core source of non-linearity in symmetric-key
block ciphers. This particular S-box is generated from the Boolean function:

```
f(X, Y, Z, W) = (Y·Z·W) ⊕ (X·Z) ⊕ (Y·W) ⊕ (Y·Z) ⊕ X
```

applied to the input and three cyclic rotations of it, giving the four output bits:

```
S(X,Y,Z,W) = ( f(X,Y,Z,W), f(Y,Z,W,X), f(Z,W,X,Y), f(W,X,Y,Z) )
```

## Requirements

- Python 3.6+

## Sample Output

```
  VERIFYING CELLULAR AUTOMATA S-BOX PROPERTIES   
Input (Bin)  ->  Output (Bin)  |  Input (Dec) -> Output (Dec)
-------------------------------------------------------------
  0000       ->     0000     |       0      ->      0
  0001       ->     0001     |       1      ->      1
  0010       ->     0010     |       2      ->      2
  0011       ->     0111     |       3      ->      7
  0100       ->     0100     |       4      ->      4
  0101       ->     1010     |       5      ->     10
  0110       ->     1110     |       6      ->     14
  0111       ->     1100     |       7      ->     12
  1000       ->     1000     |       8      ->      8
  1001       ->     1011     |       9      ->     11
  1010       ->     0101     |      10      ->      5
  1011       ->     0110     |      11      ->      6
  1100       ->     1101     |      12      ->     13
  1101       ->     0011     |      13      ->      3
  1110       ->     1001     |      14      ->      9
  1111       ->     1111     |      15      ->     15

-------------------------------------------------------------
Total Unique Outputs Found: 16 out of 16
BIJECTIVITY STATUS: TRUE (Perfect 1-to-1 Mapping!)
-------------------------------------------------------------

DIFFERENTIAL BRANCH NUMBER SCORE: 2
   (A score of 2 confirms the paper's claim of a weak diffusion profile.)
```

## What the Script Checks

| Function | Purpose |
|---|---|
| `ca_rule_131(x, y, z, w)` | The Class (1,3,1) Boolean function used to derive each output bit |
| `evaluate_sbox(input_val)` | Builds the full 4-bit S-box output by applying the rule to the input and its three cyclic rotations |
| `calculate_hamming_weight(val)` | Counts the number of set bits in a value, used for differential analysis |
| `verify_properties()` | Runs the full 16-input lookup table, checks bijectivity, and computes the differential branch number |

## Results Summary

| Property | Result | Notes |
|---|---|---|
| Bijectivity | ✅ True | All 16 inputs map to 16 unique outputs |
| Differential Branch Number | 2 | Confirms a weak worst-case diffusion path; at least one single-bit input difference produces only a single-bit output difference |

These results match the values reported in the source paper, confirming the
construction is correctly reproduced.

## References

This implementation reproduces and verifies a construction from:

> *Lightweight and Side-Channel Secure 4×4 S-Boxes from Cellular Automata Rules.*
> Ashrujit Ghoshal, Rajat Sadhukhan, Sikhar Patranabis, Nilanjan Datta, Stjepan Picek and Debdeep Mukhopadhyay
> Indian Institute of Technology, Kharagpur, India
> Delft University of Technology, The Netherlands



