��������booked,�free,�res�=�[],�list(range(n)),�[0]�*�n
��������meetings.sort()
��������for�start,�end�in�meetings:
������������while�booked�and�booked[0][0]�<=�start:
����������������_,�room�=�heappop(booked)
����������������heappush(free,�room)
������������if�free:
����������������room�=�heappop(free)
����������������heappush(booked,�(end,�room))
������������else:
����������������release,�room�=�heappop(booked)
����������������heappush(booked,�(release�+�(end�-�start),�room))
������������res[room]�+=�1
��������return�res.index(max(res))
����def�mostBooked(self,�n:�int,�meetings:�List[List[int]])�->�int:

��������return�max(freq,�key=freq.get)

2
