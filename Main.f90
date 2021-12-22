program main

implicit none

integer :: u, v, m, n, i, j
real(4),dimension(:,:), allocatable :: a
real(4),dimension(:,:), allocatable :: b
real(4) :: c(5,5)

! File unit
u = 10
v = 20

! Open the file
open(unit=u, file='M.dat', status='old')
open(unit=v, file='N.dat', status='old')

! Numbers of rows and columns
m = 5
n = 3

! Allocate the arrays
allocate( a(m,n) )

! Read data line by line
do 30 i = 1,m
  read(u, *) (a(i,j), j=1,n)
30 continue

! Display the values
write(*,*) "M matrix"
do i = 1,m
  write(*,'(3f7.2)') (a(i,:))
enddo

! The other file
! Numbers of rows and columns
m = 3
n = 5

! Allocate the arrays
allocate( b(m,n) )

! Read data line by line
do 40 i = 1,m
  read(v, *) (b(i,j), j=1,n)
40 continue

! Display the values
write(*,*) "N matrix"
do i = 1,m
  write(*,'(5f6.2)') (b(i,:))
enddo

! Close the file
close(u)
close(v)

! Call the subroutine
call matrix_multip(a,b,c)

! Display the multipled results
write(*,*) "The result"
write(*,'(5f8.2)') c

! Write to file
open(unit=50, file='MN.dat', status='replace')
write(50,'(5f9.2)') c
close(50)

! Deallocate the arrays
deallocate( a, b )

end program main