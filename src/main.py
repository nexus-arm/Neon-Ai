"""Entry point for Neon-Ai runtime and orchestration helpers."""

from modules.deployment_manager import DeploymentManager


def main() -> None:
    """Bootstrap deployment workflows with sensible defaults."""
    manager = DeploymentManager()
    manager.deploy()


if __name__ == "__main__":
    main()
