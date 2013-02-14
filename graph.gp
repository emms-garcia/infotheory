set title "Channel Simulaton"
unset key
set terminal png
set output "graph.png"
set xlabel 'Word Length'
set ylabel 'Error Percentage'
set tic scale 0
set palette defined (0 "blue", 1 "red")
set cbrange [0:1]
set cblabel "Score"
unset cbtics

set xrange [0:30]
set yrange [0:1]
set view map
plot 'output.dat' u 1:2:3 with lines palette
replot
#pause 3
