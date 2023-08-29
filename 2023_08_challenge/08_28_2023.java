class MyStack1 {
    Queue<Integer> q1;
    Queue<Integer> q2;

    public MyStack() {
        // Two queues
        q1 = new LinkedList<>(); // always contains the top of stack
        q2 = new LinkedList<>(); // contains the rest
    }

    public void push(int x) {
        if (!q1.isEmpty()) {
            q2.add(q1.remove());
        }
        q1.add(x);
    }

    public int pop() {
        int res = q1.remove();
        while (q2.size() > 1) {
            q1.add(q2.remove());
        }
        Queue<Integer> tmp;
        tmp = q1;
        q1 = q2;
        q2 = tmp;
        return res;
    }

    public int top() {
        return q1.peek();
    }

    public boolean empty() {
        return q1.isEmpty();
    }
}


class MyStack2 {
    /*
    LeetCode 225

    One queue
     */
    Queue<Integer> q;
    int top;

    public MyStack() {
        q = new LinkedList<>();
    }

    public void push(int x) {
        q.add(x);
        top = x;
    }

    public int pop() {
        for (int i = 1; i < q.size(); i++) {
            top = q.remove();
            q.add(top);
        }
        return q.remove();
    }

    public int top() {
        return top;
    }

    public boolean empty() {
        return q.isEmpty();
    }
}