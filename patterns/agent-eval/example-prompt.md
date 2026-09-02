Run the agent eval on the included shopping-cart kata.

Use N=1 trial per cell (four candidate runs). Send every candidate the same task.

Do not set or inherit a session model override.

A provider error (HTTP 5xx, RPC failure) is not a trial. Retry, then rebind that slot to another catalog model and re-run those cells. Do not rank until every cell has a completed implementation artifact. If you cannot get two models to actually run, say the eval did not complete — do not treat an API error as a model result.

When every cell has a completed trial, score each artifact, aggregate per cell, and rank the four prompt × model pairs. Say which bound models slot A and slot B used.
