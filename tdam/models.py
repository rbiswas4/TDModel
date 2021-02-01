"""

"""
__all__ = ['CompositeModel']

import sncosmo
import sfdmap


class CompositeModel(sncosmo.Model):
    def __init__(self,
                 source,
                 hostdust=sncosmo.CCM89Dust(),
                 mwdust=sncosmo.CCM89Dust(), mw_rv=3.1, host_rv=3.1):

        super().__init__(source=source,
                         effect_frames=['obs', 'rest'],
                         effect_names=['mw', 'host'],
                         effects=[mwdust, hostdust]
                        )
        
        if mw_rv is not None:
            self.set(mwr_v=mw_rv)
        if host_rv is not None:
            self.set(hostr_v=host_rv)


