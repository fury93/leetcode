�*�@param�{Array<number>}�arr
�*�@param�{number}�startIndex
�*�@yields�{number}
�*/
function*�cycleGenerator(arr,�startIndex)�{
��let�index�=�startIndex;
��while�(true)�{
����const�jump�=�yield�arr[index]
����index�=�(index�+�arr.length�+�jump�%�arr.length)�%�arr.length;
��}

}

/**
�*��const�gen�=�cycleGenerator([1,2,3,4,5],�0);
�*��gen.next().value��//�1
�*��gen.next(1).value�//�2
�*��gen.next(2).value�//�4
�*��gen.next(6).value�//�5
�*/
[1,2,3,4,5]
[1,2,6]
0
