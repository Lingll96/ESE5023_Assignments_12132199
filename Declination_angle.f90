module Declination_angle

implicit none

! ye is the given year
! lp means the leap year( 1 means ture, 0 means false)
! mo is the given month
! moda is the days in each month
! da is the given date
! ds is the accumulated days in each month
! ho is the given hour
! mi is the given minute
! d is the parameter in the formula
! sda is solar declination angel
! i,j,k are intermediate numbers
  integer :: ye, lp, mo, moda(12), da, ds(11), ho, mi, i, j
  real(4) :: d, sda, pi = 3.14159265, k

  contains

! Calculate the d
  subroutine get_d

! Judgement of leap year
    if (mod(ye,400) == 0) then
      lp = 1
    elseif ((mod(ye,100) /= 0) .and. (mod(ye,4) == 0)) then
      lp = 1
    else
      lp = 0
    endif

! Get the ds
    moda(1) = 31
    moda(3:12) = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (lp == 1) then
      moda(2) = 29
    else
      moda(2) = 28
    endif

    ds(:) = 0
    do i = 1,11
      do j = 1,i
        ds(i) = ds(i) + moda(j)
      enddo
    enddo

! Get the d
    d = ds(mo-1) + da + real(ho)/24 + real(mi)/(24*60) - 1

  end subroutine get_d

! Calculate the declination angle
  subroutine dec_ang
    sda = asin(sin((-23.44)*pi/180)*cos((360*(d + 10)*pi/(180*365.24)) + 360*0.0167*sin(360*(d - 2)*pi/(365.24*180))/pi))
  end subroutine dec_ang

end module Declination_angle