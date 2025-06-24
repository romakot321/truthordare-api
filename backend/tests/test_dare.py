from contextlib import asynccontextmanager
from typing import AsyncGenerator

import pytest
from sqlalchemy import select

from src.core.language.orm import LanguageDB
from src.dare.domain.dtos import DareReadDTO
from src.dare.infrastructure.db.orm import DareDB
from src.dare.infrastructure.db.unit_of_work import DareUnitOfWork


@pytest.mark.asyncio(loop_scope="session")
async def test_get_random_dare(test_client):
    async with _create_dare("test") as dare:
        resp = await test_client.get("/api/dare/random")
        assert resp.status_code == 200
        assert len(resp.json()) > 0


@pytest.mark.asyncio(loop_scope="session")
async def test_get_dare(test_client):
    async with _create_dare("test") as dare:
        resp = await test_client.get(f"/api/dare/{dare.id}")
        assert resp.status_code == 200
        assert resp.json() == dare.model_dump(mode="json")


@pytest.mark.asyncio(loop_scope="session")
async def test_dare_like(test_client):
    async with _create_dare("test") as dare:
        resp = await test_client.post(f"/api/dare/{dare.id}/like")
        assert resp.status_code == 204


@pytest.mark.asyncio(loop_scope="session")
async def test_dare_dislike(test_client):
    async with _create_dare("test") as dare:
        resp = await test_client.post(f"/api/dare/{dare.id}/dislike")
        assert resp.status_code == 204


@asynccontextmanager
async def _create_dare(text: str) -> AsyncGenerator[DareReadDTO]:
    uow = DareUnitOfWork()
    async with uow:
        lang = LanguageDB(title="Test")
        uow.session.add(lang)
        await uow.session.flush()

        model = DareDB(text=text, language_id=lang.id)
        uow.session.add(model)
        await uow.commit()

        yield DareReadDTO(id=model.id, text=model.text)

        await uow.session.delete(model)
        await uow.session.delete(lang)
        await uow.commit()
