
S = list(input())

answer = []
first = ""
second = ""
i = 0

while i < len(S):
    if S[i] == "<":
        for j in range(i,len(S)):
            if S[j] == ">":
                second += S[j]
                answer.append(second)
                second = ""
                break

            else:
                second += S[j]
        i = j

    else:
        if S[i] == " ":
            answer.append(S[i])


        else:
            for j in range(i, len(S)):
                if S[j] == " " or S[j] == "<":
                    answer.append(first[::-1])
                    first = ""
                    i = j-1

                    break

                elif j == len(S)-1:
                    first += S[j]
                    answer.append(first[::-1])
                    i=j

                else:
                    first += S[j]
                    i = j

    i += 1

for i in answer:
    print(i, end="")



#     if S[i] == " ":
#         stack = stack[::-1]
#         answer.append(stack)
#         stack = ""
#
#     elif S[i] == ">":
#         stack+=S[i]
#         answer.append(stack)
#         stack = ""
#
#     elif S[i] == "<":
#         for
#         stack = stack[::-1]
#         answer.append(stack)
#         stack = ""
#         stack+=S[i]
#
#     else:
#         stack+=S[i]
#
# print(newStr)
#

# str = input()
# base = ""
# newStr = []
# k = 0
# a = ""
# b = ""
# answer = []

# while True:
    # if str[k] == "<":
    #     cnt = 0
    #
    #     for i in range(k,len(str)):
    #         if str[i] == ">":
    #             cnt += 1
    #             k += cnt
    #             answer.append(a)
    #             a = ""
    #             break
    #         elif str[i] == " ":
    #             continue
    #         else:
    #             a += str[i]
    #
    #
    #         cnt += 1
    #
    # else:
    #     if str[k] == " ":
    #         break
    #     else:
    #         b += str[i]



    # k += 1



    # if str[i] == " ":
    #     newStr.append(base)
    #     base = ""
    # else:
    #     base+=str[i]
    #
    # if i == len(str)-1:
    #     newStr.append(base)
    #
    # if str[i] == "":


# print(newStr)