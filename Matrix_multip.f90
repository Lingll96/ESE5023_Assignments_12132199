subroutine matrix_multip(a,b,c)

  integer :: i, j, k
  real(4) :: a(5,3), b(3,5), c(5,5)

  c(:,:) = 0

  do i = 1,5
    do j = 1,5
      do k = 1,3
        c(i,j) = c(i,j) + a(i,k) * b(k,j)
      enddo
    enddo
  enddo


end