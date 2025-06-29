import streamlit as st

# Chaldean Numerology map
chaldean_map = {
    'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1,
    'B': 2, 'K': 2, 'R': 2,
    'C': 3, 'G': 3, 'L': 3, 'S': 3,
    'D': 4, 'M': 4, 'T': 4,
    'E': 5, 'H': 5, 'N': 5, 'X': 5,
    'U': 6, 'V': 6, 'W': 6,
    'O': 7, 'Z': 7,
    'F': 8, 'P': 8
}

def reduce_number(n):
    """Reduce to a single digit unless it's 11 or 22 (master numbers)"""
    while n > 9 and n not in [11, 22]:
        n = sum(int(digit) for digit in str(n))
    return n

def chaldean_lucky_number(name):
    name = name.upper()
    total = 0
    steps = []

    for char in name:
        if char in chaldean_map:
            value = chaldean_map[char]
            total += value
            steps.append(f"{char} = {value}")
        else:
            steps.append(f"{char} is ignored.")

    lucky_number = reduce_number(total)
    return steps, total, lucky_number

# Streamlit UI
st.title("🔮 Chaldean Numerology Lucky Number")

user_name = st.text_input("Enter your name")

if user_name:
    st.subheader(f"Lucky Number Calculation for: `{user_name}`")
    steps, total, lucky_number = chaldean_lucky_number(user_name)
    

    st.markdown("### 🔢 Calculation Steps")
    for step in steps:
        st.write(step)

    st.markdown(f"**Total Value:** `{total}`")
    st.markdown(f"🎯 **Lucky Number:** `{lucky_number}`")
    if st.button("Send balloons!"):
       st.balloons()
