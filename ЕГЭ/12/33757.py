# НАЧАЛО
#
#     ПОКА
# нашлось(01)
# ИЛИ
# нашлось(02)
# ИЛИ
# нашлось(03)
#
#         заменить(01, 30)
#
#         заменить(02, 101)
#
#         заменить(03, 202)
#
#     КОНЕЦ
# ПОКА
#
# КОНЕЦ
#

for f in range(60):
    for s in range(60):
        for t in range(60):
            st = f"0{'1' * f}{'2' * s}{'3' * t}"
            # print(st)
            while '01' in st or '02' in st or '03' in st:
                st = st.replace('01', '30', 1)
                st = st.replace('02', '101', 1)
                st = st.replace('03', '202', 1)
            if st.count('1') == 20 and st.count('2') == 10 and st.count('3') == 70:
                print(f)
