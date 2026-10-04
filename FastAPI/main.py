sub odd_even()

for i=0 to 10
cellvalue=cells(i,1).value

if cellvalue mod 2=0 then
cells(i,2).value="even"
else
cells(i,2).value="odd"
end if
next i

end sub