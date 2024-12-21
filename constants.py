from enum import Enum
from typing import Dict

class ModelProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    XAI = "xai"

class TokenLimits:
    # OpenAI Models
    GPT_4_CONTEXT = 8_192
    GPT_4_32K_CONTEXT = 32_768
    GPT_4_TURBO_CONTEXT = 128_000
    GPT_4_OUTPUT = 4_096
    GPT_35_TURBO_CONTEXT = 4_096
    GPT_35_TURBO_16K_CONTEXT = 16_384
    
    # Anthropic Models
    CLAUDE_3_OPUS_CONTEXT = 200_000
    CLAUDE_3_SONNET_CONTEXT = 100_000
    CLAUDE_3_HAIKU_CONTEXT = 50_000
    
    # Google Models
    GEMINI_15_FLASH_INPUT = 1_048_576
    GEMINI_15_FLASH_OUTPUT = 8_192
    GEMINI_15_PRO_INPUT = 2_097_152
    GEMINI_20_FLASH_INPUT = 32_000
    GEMINI_20_FLASH_OUTPUT = 8_000
    
    # XAI Models
    GROK_CONTEXT = 128_000

class RateLimits:
    # Anthropic rate limits (requests per minute, tokens per minute)
    ANTHROPIC_LIMITS = {
        "claude-3-opus": {"rpm": 5, "tpm": 10_000, "tpd": 300_000},
        "claude-3-sonnet": {"rpm": 5, "tpm": 20_000, "tpd": 300_000},
        "claude-3-haiku": {"rpm": 5, "tpm": 25_000, "tpd": 300_000},
    }

class LLMModel(Enum):
    # OpenAI Models
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo-preview"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"
    
    # Anthropic Models
    CLAUDE_3_OPUS = "claude-3-opus-20240229"
    CLAUDE_3_SONNET = "claude-3-sonnet-20240229"
    CLAUDE_3_HAIKU = "claude-3-haiku-20240229"
    
    # Google Models
    GEMINI_PRO = "gemini-pro"
    GEMINI_ULTRA = "gemini-ultra"
    
    # XAI Models
    GROK_1 = "grok-1"

# Mapping of models to their context windows
MODEL_CONTEXT_WINDOWS: Dict[LLMModel, int] = {
    LLMModel.GPT_4: TokenLimits.GPT_4_CONTEXT,
    LLMModel.GPT_4_TURBO: TokenLimits.GPT_4_TURBO_CONTEXT,
    LLMModel.GPT_3_5_TURBO: TokenLimits.GPT_35_TURBO_CONTEXT,
    LLMModel.GPT_3_5_TURBO_16K: TokenLimits.GPT_35_TURBO_16K_CONTEXT,
    LLMModel.CLAUDE_3_OPUS: TokenLimits.CLAUDE_3_OPUS_CONTEXT,
    LLMModel.CLAUDE_3_SONNET: TokenLimits.CLAUDE_3_SONNET_CONTEXT,
    LLMModel.CLAUDE_3_HAIKU: TokenLimits.CLAUDE_3_HAIKU_CONTEXT,
    LLMModel.GEMINI_PRO: TokenLimits.GEMINI_15_PRO_INPUT,
    LLMModel.GROK_1: TokenLimits.GROK_CONTEXT,
}

# Mapping of models to their providers
MODEL_PROVIDERS: Dict[LLMModel, ModelProvider] = {
    LLMModel.GPT_4: ModelProvider.OPENAI,
    LLMModel.GPT_4_TURBO: ModelProvider.OPENAI,
    LLMModel.GPT_3_5_TURBO: ModelProvider.OPENAI,
    LLMModel.GPT_3_5_TURBO_16K: ModelProvider.OPENAI,
    LLMModel.CLAUDE_3_OPUS: ModelProvider.ANTHROPIC,
    LLMModel.CLAUDE_3_SONNET: ModelProvider.ANTHROPIC,
    LLMModel.CLAUDE_3_HAIKU: ModelProvider.ANTHROPIC,
    LLMModel.GEMINI_PRO: ModelProvider.GOOGLE,
    LLMModel.GEMINI_ULTRA: ModelProvider.GOOGLE,
    LLMModel.GROK_1: ModelProvider.XAI,
}