class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        from collections import Counter

        freq = sorted([[char, count] for char, count in Counter(s).items()], reverse=True)
        sol = []
        pointer = 0

        while pointer < len(freq):
            char, count = freq[pointer]
            if count == 0:
                pointer += 1
                continue
            
            add_count = min(count, repeatLimit)

            sol.extend([char] * add_count)
            freq[pointer][1] -= add_count

            if freq[pointer][1] > 0:
                next_pointer = pointer + 1
                if next_pointer >= len(freq):
                    break
                
                next_char, next_count = freq[next_pointer]
                sol.append(next_char)
                freq[next_pointer][1] -= 1

                if freq[next_pointer][1] == 0:
                    freq.pop(next_pointer)
            else:
                pointer += 1

        return "".join(sol)

        


s = Solution()
print(s.repeatLimitedString(s = "robnsdvpuxbapuqgopqvxdrchivlifeepy", repeatLimit = 2))