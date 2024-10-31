class Solution {
    func numIdenticalPairs(_ nums: [Int]) -> Int {
    var count = 0
    var frequency = [Int: Int]()

    for num in nums {
        if let freq = frequency[num] {
            count += freq
            frequency[num] = freq + 1
        } else {
            frequency[num] = 1
        }
    }    
    return count
    }
}