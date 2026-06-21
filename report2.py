def ca_rule_131(x, y, z, w):
  
    return (y & z & w) ^ (x & z) ^ (y & w) ^ (y & z) ^ x


def evaluate_sbox(input_val):
    X = (input_val >> 3) & 1
    Y = (input_val >> 2) & 1
    Z = (input_val >> 1) & 1
    W = (input_val >> 0) & 1

    out_bit3 = ca_rule_131(X, Y, Z, W)  # S_0
    out_bit2 = ca_rule_131(Y, Z, W, X)  # S_1
    out_bit1 = ca_rule_131(Z, W, X, Y)  # S_2
    out_bit0 = ca_rule_131(W, X, Y, Z)  # S_3

    output_val = (out_bit3 << 3) | (out_bit2 << 2) | (out_bit1 << 1) | out_bit0
    return output_val


def calculate_hamming_weight(val):

    return bin(val).count('1')


def verify_properties():
    print("  VERIFYING CELLULAR AUTOMATA S-BOX PROPERTIES   ")

    outputs_seen = set()
    sbox_table = {}

    print("Input (Bin)  ->  Output (Bin)  |  Input (Dec) -> Output (Dec)")
    print("-------------------------------------------------------------")
    for i in range(16):
        out = evaluate_sbox(i)
        sbox_table[i] = out
        outputs_seen.add(out)
        print(f"  {i:04b}       ->     {out:04b}     |      {i:2d}      ->     {out:2d}")

    print("\n-------------------------------------------------------------")
    print(f"Total Unique Outputs Found: {len(outputs_seen)} out of 16")
    
    # Bijectivity Check
    if len(outputs_seen) == 16:
        print("✅ BIJECTIVITY STATUS: TRUE (Perfect 1-to-1 Mapping!)")
    else:
        print("❌ BIJECTIVITY STATUS: FALSE (Contains Duplicates)")
    print("-------------------------------------------------------------\n")

    # --- 2. CALCULATE DIFFERENTIAL BRANCH NUMBER ---
    # Formula: Min value of [ HammingWeight(in1 ^ in2) + HammingWeight(out1 ^ out2) ]
    # for all unique input pairs where in1 != in2.
    min_branch_score = 999  # Start with a high placeholder

    for in1 in range(16):
        for in2 in range(16):
            if in1 == in2:
                continue
            
            out1 = sbox_table[in1]
            out2 = sbox_table[in2]

            # Calculate differences using XOR
            input_diff = in1 ^ in2
            output_diff = out1 ^ out2

            # Count changed bits (Hamming Weights)
            w_in = calculate_hamming_weight(input_diff)
            w_out = calculate_hamming_weight(output_diff)

            branch_score = w_in + w_out
            if branch_score < min_branch_score:
                min_branch_score = branch_score

    print(f"🎳 DIFFERENTIAL BRANCH NUMBER SCORE: {min_branch_score}")
    print("   (A score of 2 confirms the paper's claim of a weak diffusion profile.)")


# Run the script
if __name__ == "__main__":
    verify_properties()