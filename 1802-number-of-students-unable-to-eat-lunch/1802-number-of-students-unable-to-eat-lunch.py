class Solution(object):
    def countStudents(self, students, sandwiches):
        cnt=True
        st=deque(students)
        sa=deque(sandwiches)

        while cnt :
            cnt=False
            for i in range(len(st)):
                if st[0] == sa[0]:
                    st.popleft()
                    sa.popleft()
                    cnt=True
                    break
                else:
                    st.append(st.popleft())

        if st:
            return len(st)
        else:
            return 0
