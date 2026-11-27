import threading
import time
from abc import ABC, abstractmethod
from typing import Optional


class ConnectionState(ABC):
    @abstractmethod
    def execute(self, conn: "PooledConnection", query: str) -> str:
        pass

    @abstractmethod
    def close(self, conn: "PooledConnection") -> None:
        pass


class IdleState(ConnectionState):
    def execute(self, conn: "PooledConnection", query: str) -> str:
        raise RuntimeError("Cannot execute query on an idle connection; acquire it first.")

    def close(self, conn: "PooledConnection") -> None:
        conn._set_state(ClosedState())


class InUseState(ConnectionState):
    def execute(self, conn: "PooledConnection", query: str) -> str:
        # TODO: Return formatted execution result: f"[Conn-{conn.conn_id}] Executed: {query}"
        pass

    def close(self, conn: "PooledConnection") -> None:
        # TODO: Transition the connection to ClosedState
        pass


class ClosedState(ConnectionState):
    def execute(self, conn: "PooledConnection", query: str) -> str:
        raise RuntimeError("Connection is permanently closed.")

    def close(self, conn: "PooledConnection") -> None:
        pass  # Idempotent close


class PooledConnection:
    def __init__(self, conn_id: int, pool: "ConnectionPool"):
        self.conn_id = conn_id
        self._pool = pool
        self._state: ConnectionState = IdleState()

    def _set_state(self, state: ConnectionState) -> None:
        self._state = state

    def execute(self, query: str) -> str:
        return self._state.execute(self, query)

    def close(self) -> None:
        self._state.close(self)

    def __enter__(self) -> "PooledConnection":
        # TODO: Transition state to InUseState and return self
        pass

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        # TODO: If connection is not closed, reset state to IdleState,
        # and return this connection back to `self._pool.release(self)`.
        # Do not suppress exceptions.
        pass


class ConnectionPool:
    def __init__(self, max_size: int = 2):
        self._condition = threading.Condition()
        self._available: list[PooledConnection] = [
            PooledConnection(i, self) for i in range(max_size)
        ]

    def acquire(self, timeout: float = 1.0) -> PooledConnection:
        # TODO: Thread-safely wait on `self._condition` until `self._available`
        # is non-empty or `timeout` expires. Pop and return a connection,
        # or raise TimeoutError if none becomes available in time.
        pass

    def release(self, conn: PooledConnection) -> None:
        # TODO: Thread-safely append `conn` back to `self._available` (if not ClosedState)
        # and notify waiting threads via `self._condition`.
        pass


# --- Verification Suite ---
if __name__ == "__main__":
    pool = ConnectionPool(max_size=1)

    with pool.acquire(timeout=0.5) as conn:
        assert conn.execute("SELECT 1") == "[Conn-0] Executed: SELECT 1"
        try:
            pool.acquire(timeout=0.1)
            assert False, "Expected TimeoutError when pool is exhausted"
        except TimeoutError:
            pass

    # Connection must be back in pool and in IdleState after exiting `with`
    reacquired = pool.acquire(timeout=0.5)
    assert isinstance(reacquired._state, IdleState)
    print("Problem 2 passed!")