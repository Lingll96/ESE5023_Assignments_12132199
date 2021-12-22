program solar_elevation_angle

use Declination_angle
use Solar_hour_angle

implicit none

! SEA_a is degree format
real(8) :: lat, SEA

! Given the time
write(*,*), "Please enter the year: "
read(*,*), ye
write(*,*), "Please enter the month: "
read(*,*), mo
write(*,*), "Please enter the date: "
read(*,*), da
write(*,*), "Please enter the hour: "
read(*,*), ho
write(*,*), "Please enter the minute: "
read(*,*), mi
write(*,*), "Please enter the longitude: "
read(*,*), lon
write(*,*), "Please enter the latitude: "
read(*,*), lat

! Call the subroutine
call get_d
call dec_ang
call get_sha

! Calculate the solar elevation angle
SEA = asin(sin(lat*pi/180)*sin(sda) + cos(lat*pi/180)*cos(sda)*cos(sha*pi/180))

! To degree
SEA = SEA*180/pi
sda = sda*180/pi
print *, " The solar elevation angle is ", SEA
print *, " The solar declination angle is ", sda
print *, " The solar hour angle is ", sha

end program solar_elevation_angle