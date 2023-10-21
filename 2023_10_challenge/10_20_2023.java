/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Node {
    int idx;
    List<NestedInteger> nested;
    public Node(int idx, List<NestedInteger> nested) {
        this.idx = idx;
        this.nested = nested;
    }
}

public class NestedIterator implements Iterator<Integer> {
    /*
    LeetCode 341

    Recursion using stack.

    4 ms, faster than 30.87%
     */
    Stack<Node> stack;
    Integer nextVal;

    public NestedIterator(List<NestedInteger> nestedList) {
        stack = new Stack<>();
        stack.push(new Node(0, nestedList));
    }

    private Integer getNext() {
        if (stack.isEmpty()) return null;
        Node cur = stack.pop();
        if (cur.idx + 1 < cur.nested.size()) {
            stack.push(new Node(cur.idx + 1, cur.nested));
        }
        if (cur.idx < cur.nested.size() && cur.nested.get(cur.idx).isInteger())
            return cur.nested.get(cur.idx).getInteger();
        if (!cur.nested.isEmpty())
            stack.push(new Node(0, cur.nested.get(cur.idx).getList()));
        return getNext();
    }

    @Override
    public Integer next() {
        hasNext();
        Integer tmp = nextVal;
        nextVal = null;
        return tmp;
    }

    @Override
    public boolean hasNext() {
        if (nextVal == null) nextVal = getNext();
        return nextVal != null;
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */



/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */

public class NestedIterator implements Iterator<Integer> {
    /*
    LeetCode 341

    Much better recursion. 4 ms, faster than 30.87%
     */
    Stack<NestedInteger> stack;

    public NestedIterator(List<NestedInteger> nestedList) {
        stack = new Stack<>();
        stack.push(new Node(0, nestedList));
    }

    private void expand(List<NestedInteger> nested) {
        for (int i = nested.size() - 1; i >= 0; i--) stack.push((nested.get(i)));
    }

    @Override
    public Integer next() {
        if (hasNext())
            return stack.pop().getInteger();
        return null;
    }

    @Override
    public boolean hasNext() {
        if (stack.isEmpty()) return false;
        if (stack.get(stack.size() - 1).isInteger()) return true;
        expand(stack.pop().getList());
        return hasNext();
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */

