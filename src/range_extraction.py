# Range Extraction from CodeWars
import codewars_test as test

def check_next_plus_one_v1(array, position):
    if array[position] - array[position+1] == -1:
        out = True
    else:
        out = False
    return out

def check_next_plus_one(array, position):
    return True if array[position] - array[position+1] == -1 else False

def check_two_next_plus_one(array, position):
    return True if check_next_plus_one(array, position) == True and check_next_plus_one(array, position+1) == True else False

def solution_alexis(args):
    position = 0
    out = ''
    while position < len(args)-2:
        if check_two_next_plus_one(args, position) == False:
            out = out+','+str(args[position])
            position += 1
            # if position == len(args)-2:
            #     out = out+','+str(args[position])+','+str(args[position+1])
        else:
            out = out+','+str(args[position])+'-'
            while check_next_plus_one(args, position) == True and position < len(args)-2:
                position += 1
            if position == len(args)-2 and check_next_plus_one(args, position-1) == True:
                position = len(args)-1
            out = out+str(args[position])
            position +=1
    if position < len(args)-1:
        out = out+','+str(args[position])+','+str(args[position+1])
        position += 2
    if position < len(args):
        out = out+','+str(args[position])
        position += 1
    return(out[1:])

def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)

# @test.describe("Range extraction")
# def desc1():

#     @test.it("Sample Tests")
#     def it1():
#         test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
#         test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')

array_1 = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
array_2 = [-3,-2,-1,2,10,15,16,18,19,20]
array_3 = [-79, -78, -76, -75, -74, -73, -72, -69, -67, -64, -63, -60]   # '-79,-78,-76--72,-69,-67,-64,-63,-60'
array_4 =  [-87, -86, -85, -83, -82, -79, -77, -75, -73, -72, -69, -66, -65, -62, -60, -59]
array_5 = [-69, -66, -65, -63, -61, -59, -58, -55, -54, -53, -51, -48, -45, -43, -40, -39, -38, -37, -36, -34, -31, -28, -26, -25, -24, -21, -18]
array_6 =  [-65, -62, -59, -58, -55, -53, -52, -49, -46, -43, -40, -39, -38, -35, -32, -30, -29, -27, -25]
array_7 = [-86, -84, -83, -82, -81, -78, -76, -75, -73, -70, -69, -67, -65, -62, -61, -59, -56, -53, -52, -51, -50, -49, -48, -45, -43, -41, -39, -36, -33, -32]

print(solution(array_7))
