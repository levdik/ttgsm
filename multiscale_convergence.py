from diffraction_solver import solve_diffraction
from incidence import Incidence
from grating import Grating
import logging
import sys


logging.basicConfig(filename='multiscale.log', filemode='w', format='%(message)s')

try:
    if len(sys.argv) == 1:
        print('n range:', end='\t')
        n_range = list(map(int, input().split(',')))
        print('d range from:', end='\t')
        d_from = int(input())
        print('d range to:', end='\t')
        d_to = int(input())
        print('thickness:', end='\t')
        thickness = float(input())
        print('accuracy:', end='\t')
        accuracy = float(input())
        print('num sweeps:', end='\t')
        nswp = int(input())
    else:
        n_range = list(map(int, sys.argv[1].split(',')))
        d_from = int(sys.argv[2])
        d_to = int(sys.argv[3])
        thickness = float(sys.argv[4])
        accuracy = float(sys.argv[5])
        nswp = int(sys.argv[6])

    d_range = range(d_from, d_to)

    smaller_scale = 6.3

    for d in d_range:
        for n in n_range:

            incidence = Incidence(angle=10)
            grating = Grating.multiscale_lamellar_random(period=n * smaller_scale, n=n,
                                                         thickness=thickness, max_permittivity=2.1, seed=1)
            x = solve_diffraction(
                do=d,
                dl=d,
                grating=grating,
                incidence=incidence,
                accuracy=accuracy,
                nswp=nswp
            )

            amp = abs(x.full(asvector=True)[2 ** (d - 1)])
            # print(n, d, amp)
            logging.warning(f'{n} {d} {1 - amp}')
except Exception as e:
    logging.warning(e)
