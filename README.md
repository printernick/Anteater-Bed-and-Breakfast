**PROJECT DESCRIPTION AND SAMPLE INPUTS WRITTEN BY DAVID KAY

The Anteater Bed and Breakfast is a program that keeps track of reservations
at "AntBnB", a small "bed and breakfast" hotel.

UCI has just started a program in hotel and restaurant management; 
its dean has established a small "bed and breakfast" hotel as a lab for the program's students. 
The dean has asked you to write the reservations software for this new inn, 
which will be called the Anteater BandB.

<pre>

NB
	(for "add a new bedroom") followed by an integer room number (in the range 1–999). Add a new bedroom with the specified room number.
LB
	(for "list bedrooms"). Print a list of the bedrooms currently available. The input file may contain any number of these commands in 
  any order; each LB command prints a list of available bedrooms based on what has been added as of that point. The room list is 
  outputted in order by room number.

PL
  (for "print line"), followed by any text. Simply print (or "echo") a line, copying the input (not counting the PL and leading 
  whitespace) to the output. You'll find it useful in testing, and it's also a simple way to make the program's reports clearer or 
  fancier.
  
**
  Comment, followed by any text. Like comments in a program, comment lines don't have any effect on the program's behavior; they just 
  serve as annotations in the command file.
  
DB
  (for "delete bedroom"), followed by a bedroom number. Delete the specified room from the list. Print an error message if the specified 
  room isn't on the list.
  
RR
  (for "reserve room") followed by a bedroom number, then an arrival date in the form mm/dd/yyyy, then a departure date in the form 
  mm/dd/yyyy, then the guest's name): Add a new reservation for the specified room on the specified dates.
  
LR
  (for "list reservations"). Print all the reservations.
DR
  (for "delete reservation"), followed by the confirmation number of a reservation. Deletes the specified reservation. If a DR command 
  gives a confirmation number that isn't in the list of reservations, your program should produce an error message.
  
RB
  (for "reservations by bedroom"), followed by a number. Lists all reservations for a given bedroom.
RG
  (for "reservations by guest"), followed by a string. List all reservations for a given guest.
LA
  (for "list arrivals"), followed by a date in the same mm/dd/yyyy form as before. Print a list of all guests arriving on the specified 
  date.
LD
  (for "list departures"), followed by a date in the same mm/dd/yy form as before. Print a list of all guests departing on the specified 
  date.
LF
  (for "list free bedrooms"), followed by two dates. List all bedrooms that are free each night for a guest arriving on the first date 
  and departing on the second.
LO
  (for "list occupied bedrooms"), followed by two dates. List all bedrooms that are occupied for at least one night between the given 
  arrival and departure dates.
 
</pre>

NOTE: David Kay intended output to be written to a file, but my program prints
to the console.
