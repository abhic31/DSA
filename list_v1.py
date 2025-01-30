class Mylist:
    def __init__(self):
        pass
    
    def clear_list(self,l:list):
        l.clear()
        return l
    
    def reverse_list(self,l:list):
        l.reverse()
        # l[::-1] second method to reverse
        # list(reversed(l)) third method
        return l
    
    def sum_elements_list(self,l:list):
        # sum(list) : option 1
        count = 0 
        for i in l:
            count += 1
        return count
    
    def multiply_all_number(self,l:list):
        mul = 1
        for i in l:
            mul = mul * i
        return mul
    
    def smallest_number(self,l:list):
        #min(l) - one method
        # l.sort() --> gets list sorted and fetch first element
        smallest = l[0]
        for i in l:
            if i < smallest:
                smallest = i
        return smallest
    
    def largest_element(self,l:list):
        #max(l) - one method
        # l.sort() --> gets list sorted and fetch last element
        largest = l[-1]
        for i in l:
            if i > largest:
                largest = i
        return largest
    
    def second_larget(self,l:largest_element):
        # l.sort(reverse = True) one method
        first , second = float('-inf'),float('-inf')
        for num in l:
            if num > first:
                second = first
                first = num
            elif num > second and num!=first:
                second = num
        return second if second != float('-inf') else None
    
    def N_largest_element(self,l:list,N:int):
        final_list = []
        for i in range(0,N):
            max1 = 0
            
            for j in range(len(l)):
                if l[j] > max1:
                    max1 = l[j]
            l.remove(max1)
            final_list.append(max1)
        return final_list
    
    def remove_multiple_elements(self,l:list,l2:list):
        res = []
        for i in l:
            if i not in l2:
                res.append(i)
        return res
    
    def copy_list(self,l:list):
        copy_list = l.copy()
        # copy_list = l[:] another method
        # copy_list = list(l) another method
        return copy_list
    
    def count_occurance_of_element(self,l:list,element):
        # l.count(element) one method
        count = 0
        for i in l:
            if i == element:
                count += 1
        return count
    
    def duplicates_integers(self,l:list):
        seen = set()
        dup = []
        for i in l:
            if i in seen:
                dup.append(i)
            else:
                seen.add(i)
        return dup
    
    def cumlative_sum(self,l:list):
        total = 0 
        cumlative_sum = []
        for i in l:
            total = total + i
            cumlative_sum.append(total)
        return cumlative_sum
    
    def sum_numbers_digits(self,l:list):
        total_sum = sum(sum(int(digit) for digit in str(number)) for number in l)
        return total_sum
        
    
    
        

mylist = Mylist()
l = [233,444,2233,2323]
print(mylist.sum_numbers_digits(l))
