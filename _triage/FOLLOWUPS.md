# Follow-ups across batches

References that a batch could not make yet because the target belongs to a later batch. The batch that creates the target resolves its rows, adding the `depends_on` or `assumes` entries and replacing the plain-text mentions with links, and then deletes them from this file. The file must be empty before `_triage/` is deleted.

| Created by | Node(s) to update | Missing target (legacy ID, owning batch) | What to add |
|---|---|---|---|
