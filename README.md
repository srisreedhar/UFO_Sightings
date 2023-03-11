# UFO_Sightings

![Project Aquarius](https://thinkaboutit.site/ufos/wp-content/uploads/sites/12/2012/12/54carpet.gif "Aquarius")

The [NATIONAL UFO Reporting Center](https://nuforc.org/databank/) maintains an Online repository of all the UFO sightings which is currently limited to state of USA.
There are four types of indexed datasets available : <br>
[Index by EVENT DATE](https://nuforc.org/webreports/ndxevent.html)  
[Index by STATE](https://nuforc.org/webreports/ndxloc.html)  
[Index by SHAPE OF UFO](https://nuforc.org/webreports/ndxshape.html)  
[Index by DATE POSTED](https://nuforc.org/webreports/ndxpost.html)

This is a Hobby Project to get that data and visualize how it looks like :)

# Files & Folders

-  **ndxevent.py** : gets all events data

-  **ndxloc.py** : gets all location based data

-  **ndxshape.py** : data related to shape of the UFO

-  **scheduler.py** : Monthly/Weekly checker, that checks for updates on nuforc and updates `airflow-wip`
- datacheck.py : data sanity checker / logger  `wip`

-  **/data** : folder which has the initial version of the gathered data

# Plan & Execution

>I did not want to use the libraries like BeautifulSoup/lxml that makes my life simpler,I just want to write as many lines of raw code as possible to make this work.


```mermaid
graph TD
A[nuforc.org DataBank ] -- Extract  --> B((Store Raw Files))
A -- Transformed Data--> C(Transform)
B --> J{Final Data Repository}
C --> D[Events +]
C --> E[States +]
C --> F[Shapes +] 
C --> H[Aggregations/KPIs]
D  --> I((Final Transformed Data))
E --> I
F --> I
H --> I
I -- Load--> J
J --> K(LookerStudio/Streamlit)

```



![UFO](https://res.cloudinary.com/teepublic/image/private/s--L0c69ARe--/t_Preview/b_rgb:191919,c_lpad,f_jpg,h_630,q_90,w_1200/v1592599322/production/designs/11490920_0.jpg "UFO")





