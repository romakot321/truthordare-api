from contextlib import asynccontextmanager
from typing import AsyncGenerator

import pytest
from sqlalchemy import select

from src.core.language.orm import LanguageDB
from src.truth.domain.dtos import TruthReadDTO
from src.truth.infrastructure.db.orm import TruthDB
from src.truth.infrastructure.db.unit_of_work import TruthUnitOfWork


@pytest.mark.asyncio(loop_scope="session")
async def test_get_random_truth(test_client):
    async with _create_truth("test") as truth:
        resp = await test_client.get("/api/truth/random")
        assert resp.status_code == 200
        assert len(resp.json()) > 0


@pytest.mark.asyncio(loop_scope="session")
async def test_get_truth(test_client):
    async with _create_truth("test") as truth:
        resp = await test_client.get(f"/api/truth/{truth.id}")
        assert resp.status_code == 200
        assert resp.json() == truth.model_dump(mode="json")


@pytest.mark.asyncio(loop_scope="session")
async def test_truth_like(test_client):
    async with _create_truth("test") as truth:
        resp = await test_client.post(f"/api/truth/{truth.id}/like")
        assert resp.status_code == 204


@pytest.mark.asyncio(loop_scope="session")
async def test_truth_dislike(test_client):
    async with _create_truth("test") as truth:
        resp = await test_client.post(f"/api/truth/{truth.id}/dislike")
        assert resp.status_code == 204


@asynccontextmanager
async def _create_truth(text: str) -> AsyncGenerator[TruthReadDTO]:
    uow = TruthUnitOfWork()
    async with uow:
        lang = LanguageDB(title="Test")
        uow.session.add(lang)
        await uow.session.flush()

        model = TruthDB(text=text, language_id=lang.id)
        uow.session.add(model)
        await uow.commit()

        yield TruthReadDTO(id=model.id, text=model.text)

        await uow.session.delete(model)
        await uow.session.delete(lang)
        await uow.commit()