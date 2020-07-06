"""
Modification of redshift from the cosmological redshift
"""
__all__ = ["zs_pec"]


from astropy.constants import c


def zs_pec(zcosmo, vpecoverthousand):
    """
    the spectroscopic redshift measured accounting for the peculiar velocity of the
    astrophysical source along the line of sight

    Parameters
    ----------
    zcsosmo : float, or np.ndarray(float)
        the cosmological redshifts (1./a -1 ) in a FRW metric
    vpecoverthousand : float, or np.ndarray of type float
        the peculiar velocity along the line of sight in units of 1000 km/s with
        positive values corresponding to a direction away from the observer.


    Returns
    -------
    zs_pec : `np.ndarray`
        The spectroscopic redshift which is different from the cosmological redshift due to the peculiar
        velocity
    """

    zcosmo = np.ravel(zcosmo)
    zs_pec = zcosmo + vpecoverthousand * 1.0e6 / c.value * (zcosmo + 1)

    return zs_pec
