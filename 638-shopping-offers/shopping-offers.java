class Solution {
    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        Map<String, Integer> memo = new HashMap<>();
        return dfs(price, special, needs, memo);
    }

    private int dfs(List<Integer> price, 
        List<List<Integer>> special, 
        List<Integer> needs,  
        Map<String, Integer> memo){

        if(areFullfilled(needs))
            return 0;
        if(memo.containsKey(needs.toString())){
            return memo.get(needs.toString());
        }
        int min = Integer.MAX_VALUE;
        //try all the coupons
        for(int i=0;i<special.size();i++){
            //if coupon can be applied
            if(isValid(needs, special.get(i))){
                int p = remove(special.get(i), needs);
                min = Math.min(min, p + dfs(price, special, needs, memo));
                add(special.get(i), needs);
            }
            int tp = getTotalPrice(price, needs);
            min = Math.min(min, tp + dfs(price, special, new ArrayList<>(), memo));
        }
        memo.put(needs.toString(), min);
        return min;

    }

    private int getTotalPrice(List<Integer> price, List<Integer> needs){
        int sum = 0;
        for(int i=0;i<needs.size();i++){
            sum = sum + needs.get(i) * price.get(i);
        }
        return sum;
    }

    private boolean areFullfilled(List<Integer> needs){
        for(int need: needs){
            if(need!=0){
                return false;
            }
        }
        return true;
    }

    private int remove(List<Integer> coupon, List<Integer> needs){
        int i=0;
        for(;i<needs.size();i++){
            needs.set(i, needs.get(i) - coupon.get(i));
        }
        return coupon.get(i);
    }

    private int add(List<Integer> coupon, List<Integer> needs){
        int i=0;
        for(;i<needs.size();i++){
            needs.set(i, needs.get(i) + coupon.get(i));
        }
        return coupon.get(i);
    }

    private boolean isValid(List<Integer> needs, List<Integer> coupon){
        for(int i=0;i<needs.size();i++){
            if(coupon.get(i)> needs.get(i)){
                return false;
            }
        }
        return true;
    }
}