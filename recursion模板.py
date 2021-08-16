
"""第一遍，看题目，想解法，如果十几分分想不出来直接看题解，看看别人的解法，最好能够默写出来
第二遍，自己尝试写出
第三遍，隔几天后再次写一下，体会+上自己的优化
第四遍，一周过去后，再来一一遍
第五遍，复习，例如面试前。 (不一定是五遍，而是要做出来自己的体会和思考才是最重要的。)"""
def recursion(param, level):
    if level > MAXLEVEL:
        return

    process(param, level)

    recursion(newparam, level+1)

    # reverse state