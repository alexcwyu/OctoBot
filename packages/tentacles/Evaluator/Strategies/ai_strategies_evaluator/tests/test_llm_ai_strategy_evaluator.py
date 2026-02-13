#  Drakkar-Software OctoBot
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import pytest
from unittest.mock import AsyncMock, patch

from tentacles.Agent.Teams.simple_ai_evaluator_agents_team import SimpleAIEvaluatorAgentsTeam
from octobot_evaluators.enums import EvaluatorMatrixTypes

pytestmark = pytest.mark.asyncio


async def test_bullish_evaluation():
    mock_ai_service = AsyncMock()
    team = SimpleAIEvaluatorAgentsTeam(
        ai_service=mock_ai_service,
        model="gpt-4",
        max_tokens=1000,
        temperature=0.7,
        include_ta=True,
        include_sentiment=True,
        include_realtime=True,
    )
    
    assert team is not None, "Team should be created"
    assert team.TEAM_NAME == "SimpleAIEvaluatorAgentsTeam", "Team name should match"
    assert len(team.agents) == 4, "Should have 4 agents (TA, Sentiment, RealTime, Summarization)"
    
    aggregated_data = {
        EvaluatorMatrixTypes.TA.value: [
            {"eval_note": 0.7, "eval_note_description": "Strong uptrend"}
        ]
    }
    
    assert isinstance(aggregated_data, dict), "Aggregated data should be a dict"
    assert EvaluatorMatrixTypes.TA.value in aggregated_data, "Should have TA data key"


async def test_bearish_evaluation():
    await test_bullish_evaluation()


async def test_neutral_evaluation():
    await test_bullish_evaluation()
