<h1> Log report </h1>
<table border = '1' , bgcolor = 'green'>
%for ip,dt,im,url in res:
%if  im == 'no image':
<tr bgcolor = 'yellow'>
   <td>{{ip}}</td>
   <td>{{dt}}</td>
   <td bgcolor = 'red'>{{im}}</td>
   <td>{{url}}</td>
</tr>
%else:
 <tr>
   <td>{{ip}}</td>
   <td>{{dt}}</td>
   <td bgcolor = 'red'>'No image'</td>
   <td>{{url}}</td>
</tr>
%end
%end
</table>