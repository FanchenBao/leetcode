class Food {
    int rating;
    String name;

    Food(String name, int rating) {
        this.rating = rating;
        this.name = name;
    }
}

class FoodComparator implements Comparator<Food> {
    @Override
    public int compare(Food x, Food y) {
        if (x.rating > y.rating) // max heap for rating
            return -1;
        if (x.rating < y.rating)
            return 1;
        return x.name.compareTo(y.name); // min heap for name
    }
}


class FoodRatings {
    /*
    LeetCode 2353

    A fairly involved priority queue problem. The main issue is with the syntax
    of Java to get the priority queue to work. Another problem is to figure out
    how to update a priority queue when its element is changed. The priority
    queue does not automatically update itself once its element is updated,
    hence we have to always push in the new value and examine the top of the
    queue and discard any element that has outdated values -- very similar to
    how Dijkstra works.

    O(NlogN) for the constructor.
    O(logN) for changeRating
    O(logN) for highestRating

    */
    Map<String, PriorityQueue<Food>> cuisineRatings = new HashMap<>();
    Map<String, Integer> foodRatings = new HashMap<>();
    Map<String, String> foodCuisines = new HashMap<>();

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        for (int i = 0; i < foods.length; i++) {
            cuisineRatings.putIfAbsent(cuisines[i], new PriorityQueue<>(10000, new FoodComparator()));
            foodRatings.put(foods[i], ratings[i]);
            foodCuisines.put(foods[i], cuisines[i]);
            cuisineRatings.get(cuisines[i]).add(new Food(foods[i], ratings[i]));
        }
    }

    public void changeRating(String food, int newRating) {
        foodRatings.put(food, newRating);
        cuisineRatings.get(foodCuisines.get(food)).add(new Food(food, newRating));
    }

    public String highestRated(String cuisine) {
        PriorityQueue<Food> pq = cuisineRatings.get(cuisine);
        while (!pq.isEmpty()) {
            Food topFood = pq.peek();
            if (topFood.rating != foodRatings.get(topFood.name))
                pq.poll();
            else
                break;
        }
        return pq.peek().name;
    }
}


/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */
