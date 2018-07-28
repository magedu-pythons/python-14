#!/usr/bin/env python
#.Author:Dyw
lst="""
In August of 1993 my father was diagnosed with inoperable lung cancer. 
He chose not to receive chemotherapy treatments so that he could live out the rest of his life in dignity. 
About a week before his death, we asked Dad if he would play the mandolin for us. 
He made excuses but said "okay". He knew it would probably be the last time he would play for us. 
He tuned up the old mandolin and played a few notes. When I looked around, there was not a dry eye in the family. 
We saw before us a quiet humble man with an inner strength that comes from knowing God, and living with him in one's life. 
Dad would never play the mandolin for us again. We felt at the time that he wouldn't have enough strength to play, and that makes the memory of that day even stronger. 
Dad was doing something he had done all his life, giving. As sick as he was, he was still pleasing others. Dad sure could play that Mandolin!
"""
lst1=lst.split()
setnum = list(set(lst1))
count = 0
for i in setnum:
    print(i ,":\t",lst1.count(i))