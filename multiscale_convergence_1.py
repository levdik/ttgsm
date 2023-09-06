from diffraction_solver import solve_diffraction
from incidence import Incidence
from grating import Grating


if __name__ == '__main__':
    smaller_scale = 6.3
    n_range = [1, 10, 20, 30]
    d_range = range(2, 17)

    for d in d_range:
        for n in n_range:

            incidence = Incidence(angle=10)
            grating = Grating.multiscale_lamellar_random(period=n * smaller_scale, n=n,
                                                     thickness=0.25, max_permittivity=2.1, seed=1)
            x = solve_diffraction(d, d, grating, incidence, accuracy=1e-5)
            amp = abs(x.full(asvector=True)[2 ** (d - 1)])
            print(n, d, amp)
