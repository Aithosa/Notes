#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/matrix_proxy.hpp>
#include <boost/numeric/ublas/vector_proxy.hpp>
 
//#include <iostream>
 
namespace ublas = boost::numeric::ublas;
 
int main(int argc, char ** argv)
{
    ublas::matrix<double> M(3, 3, 1);
    ublas::identity_matrix<double> I(3);
    ublas::zero_matrix<double> Z(3);
    ublas::scalar_matrix<double> S(2, 3);
 
    for (size_t idxRow = 0; idxRow < M.size1(); idxRow++)
    {
        for (size_t idxCol = 0; idxCol < M.size2(); idxCol++)
        {
            M(idxRow, idxCol) = 3 * idxRow + idxCol;
        }
    }
 
    std::cout << "M: " << M << std::endl;
    std::cout << ublas::row(M, 0) << std::endl;
    std::cout << ublas::inner_prod(ublas::row(M, 0), ublas::row(M, 1)) << std::endl;
    std::cout << ublas::project(ublas::row(M, 1), ublas::range(0, 2)) << std::endl;
 
    getchar();
 
    return 0;
}