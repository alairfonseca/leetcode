# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    result = 0
    
    prices.each_with_index { |val, idx|
        if idx < prices.length - 1 and prices[idx] < prices[idx + 1] then
            result += prices[idx + 1] - prices[idx]
        end
    }
        
    result
end