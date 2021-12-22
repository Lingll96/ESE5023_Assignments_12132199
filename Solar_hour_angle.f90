module Solar_hour_angle

!implicit none

! TZ is the difference in the local time zone to the UTC
! LST is the local solar time
! cLST is the corrected one
! EOT is the equatio of time
! sha is solar hour angle

  use Declination_angle

  integer(4) :: TZ
  real(4) :: LST, cLST, EOT, lon, sha, gama

  contains

! Calculate the solar hour angle
  subroutine get_sha

! Calculate the LST
    LST = ho + real(mi)/60

! Calculate EOT
    gama = (floor(d) - 1 + (ho - 12)/24)*2*pi/365.0
    EOT = 229.18 * (0.000075 + 0.001868*cos(gama) - 0.032077*sin(gama) - 0.014615*cos(2*gama) - 0.040849*sin(2*gama))

! Calculate TZ
    if (mod(lon,15.0) <= 7.5)  then
      TZ = floor(lon/15)
    else
      TZ = floor(lon/15) + 1
    endif

! Calculate cLST
    cLST = LST + (EOT + 4*(lon - 15*real(TZ)))/60

    sha = 15*(cLST - 12)

  end subroutine get_sha

end module Solar_hour_angle