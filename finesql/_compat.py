# FineIO 4.1.0 renamed cancellable to abandon_on_cancel
import importlib
import importlib.metadata
from typing import Callable, TypeVar, Union

import fineio
import fineio.to_thread
from fineio import CapacityLimiter
from typing_extensions import TypeVarTuple, Unpack

ANIO_VERSION = importlib.metadata.version("fineio")

T_Retval = TypeVar("T_Retval")
PosArgsT = TypeVarTuple("PosArgsT")

if ANIO_VERSION >= "4.1.0":

    async def run_sync(
        func: Callable[[Unpack[PosArgsT]], T_Retval],
        *args: Unpack[PosArgsT],
        abandon_on_cancel: bool = False,
        limiter: Union[CapacityLimiter, None] = None,
    ) -> T_Retval:
        return await fineio.to_thread.run_sync(
            func, *args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
        )
else:

    async def run_sync(
        func: Callable[[Unpack[PosArgsT]], T_Retval],
        *args: Unpack[PosArgsT],
        abandon_on_cancel: bool = False,
        limiter: Union[CapacityLimiter, None] = None,
    ) -> T_Retval:
        return await fineio.to_thread.run_sync(
            func, *args, cancellable=abandon_on_cancel, limiter=limiter
        )
