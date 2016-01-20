#divide and conquer
`
Alogrithms Result M(Problem prob)
{
    if (<problem can be solved easily>)
        return <easy solution>;
    // The problem cannot be solved easily.
    Problem smaller1 = <reduce problem to smaller problem>
    Result result1 = M(smaller1);
    Problem smaller2 = <reduce problem to smaller problem>
    Result result2 = M(smaller2);
    ...
    Result finalResult = <combine all results of smaller problem to solve large problem>
    return finalResult;
}
`
