/**�
�*�@param�{number}�target
�*�@return�{number}
�*/
Array.prototype.upperBound�=�function(target)�{
����return�this.lastIndexOf(target)
};


//�[3,4,5].upperBound(5);�//�2
//�[1,4,5].upperBound(2);�//�-1
//�[3,4,6,6,6,6,7].upperBound(6)�//�5
[3,4,5]
5
[1,4,5]
