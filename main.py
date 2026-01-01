#!/usr/bin/env python3
"""
Multilingual Content Localizer - Llama-Based Localization AI
Adapts content linguistically and culturally for different markets
Author: Pranay M
"""

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.markdown import Markdown
import json

console = Console()

MARKETS = {
    1: ("US", "United States", "en-US"),
    2: ("UK", "United Kingdom", "en-GB"),
    3: ("ES", "Spain", "es-ES"),
    4: ("MX", "Mexico", "es-MX"),
    5: ("FR", "France", "fr-FR"),
    6: ("DE", "Germany", "de-DE"),
    7: ("JP", "Japan", "ja-JP"),
    8: ("CN", "China", "zh-CN"),
    9: ("BR", "Brazil", "pt-BR"),
    10: ("IN", "India", "hi-IN"),
    11: ("SA", "Saudi Arabia", "ar-SA"),
    12: ("KR", "South Korea", "ko-KR")
}

CONTENT_TYPES = ["marketing", "legal", "technical", "website", "app", "social_media", "email"]

class ContentLocalizer:
    def __init__(self, model: str = "llama3.2"):
        self.model = model
        self.source_market = "US"
        self.target_market = None
        self.brand_guidelines = None
    
    def set_target_market(self, market_id: int):
        if market_id in MARKETS:
            self.target_market = MARKETS[market_id]
            return True
        return False
    
    def localize_content(self, content: str, content_type: str = "marketing") -> dict:
        if not self.target_market:
            return {"error": "Target market not set"}
        
        target_code, target_name, locale = self.target_market
        
        prompt = f"""Localize this {content_type} content for {target_name} ({locale}).

Original Content:
{content}

Perform complete localization:
1. Language translation
2. Cultural adaptation
3. Local references and examples
4. Appropriate tone for market
5. Date/time/currency formats
6. Local idioms and expressions

Return JSON:
{{
    "original": "original text",
    "localized": "fully localized text",
    "locale": "{locale}",
    "adaptations": [
        {{
            "original_element": "what was changed",
            "localized_element": "what it became",
            "reason": "why changed"
        }}
    ],
    "cultural_notes": ["important cultural considerations"],
    "warnings": ["potential sensitivities"],
    "alternative_versions": ["if multiple valid approaches"],
    "quality_score": 90
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def cultural_analysis(self, content: str) -> dict:
        if not self.target_market:
            return {"error": "Target market not set"}
        
        target_code, target_name, locale = self.target_market
        
        prompt = f"""Analyze cultural appropriateness of this content for {target_name}.

Content:
{content}

Return JSON:
{{
    "overall_appropriateness": "appropriate/needs_changes/inappropriate",
    "cultural_issues": [
        {{
            "issue": "identified issue",
            "severity": "critical/moderate/minor",
            "location": "where in content",
            "explanation": "why problematic",
            "suggestion": "how to fix"
        }}
    ],
    "positive_elements": ["culturally appropriate elements"],
    "missing_elements": ["cultural elements to add"],
    "taboos_detected": ["potential taboos"],
    "local_preferences": {{
        "color_implications": "color meanings in culture",
        "number_implications": "lucky/unlucky numbers",
        "imagery_notes": "visual considerations"
    }},
    "competitive_context": "how competitors localize",
    "recommendations": ["prioritized recommendations"]
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def adapt_marketing(self, campaign: str) -> dict:
        if not self.target_market:
            return {"error": "Target market not set"}
        
        target_code, target_name, locale = self.target_market
        
        prompt = f"""Adapt this marketing campaign for {target_name} ({locale}).

Campaign:
{campaign}

Return JSON:
{{
    "adapted_campaign": {{
        "headline": "localized headline",
        "tagline": "localized tagline",
        "body_copy": "localized body",
        "cta": "localized call-to-action"
    }},
    "messaging_adjustments": [
        {{
            "original_message": "original",
            "adapted_message": "adapted",
            "cultural_rationale": "why changed"
        }}
    ],
    "visual_recommendations": {{
        "imagery_changes": ["recommended image changes"],
        "color_adjustments": ["color modifications"],
        "layout_changes": ["layout recommendations"]
    }},
    "channel_recommendations": {{
        "preferred_channels": ["best channels for market"],
        "avoid_channels": ["channels to avoid"],
        "timing": "best times to reach audience"
    }},
    "local_influencers": "influencer marketing approach",
    "compliance_notes": ["regulatory considerations"],
    "budget_considerations": "market-specific budget notes"
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def localize_ui(self, ui_strings: dict) -> dict:
        if not self.target_market:
            return {"error": "Target market not set"}
        
        target_code, target_name, locale = self.target_market
        
        prompt = f"""Localize these UI strings for {target_name} ({locale}).

UI Strings:
{json.dumps(ui_strings, indent=2)}

Return JSON:
{{
    "localized_strings": {{
        "key": "localized value"
    }},
    "length_warnings": [
        {{
            "key": "string key",
            "original_length": 10,
            "localized_length": 15,
            "issue": "may overflow UI"
        }}
    ],
    "rtl_considerations": "if RTL language",
    "pluralization_rules": "plural forms needed",
    "formatting_notes": ["date/time/number formats"],
    "context_requests": ["strings needing more context"]
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def transcreate_slogan(self, slogan: str) -> dict:
        if not self.target_market:
            return {"error": "Target market not set"}
        
        target_code, target_name, locale = self.target_market
        
        prompt = f"""Transcreate this slogan/tagline for {target_name} ({locale}).

Original Slogan: {slogan}

Transcreation means creative adaptation, not literal translation.
Preserve the emotional impact and brand essence.

Return JSON:
{{
    "original": "{slogan}",
    "transcreations": [
        {{
            "version": "transcreated slogan",
            "approach": "literal/adaptive/creative",
            "emotional_impact": "preserved emotion",
            "cultural_resonance": "how it connects locally",
            "confidence": 85
        }}
    ],
    "recommended_version": "best option",
    "reasoning": "why this is best",
    "alternatives_rejected": [
        {{
            "version": "rejected option",
            "reason": "why not chosen"
        }}
    ],
    "testing_recommendations": "how to validate"
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def localize_legal(self, legal_text: str) -> dict:
        if not self.target_market:
            return {"error": "Target market not set"}
        
        target_code, target_name, locale = self.target_market
        
        prompt = f"""Localize legal content for {target_name} ({locale}).

Legal Text:
{legal_text}

Return JSON:
{{
    "localized_text": "translated legal text",
    "legal_adaptations": [
        {{
            "original_clause": "original",
            "adapted_clause": "adapted",
            "legal_basis": "local law reference"
        }}
    ],
    "compliance_requirements": [
        {{
            "requirement": "local requirement",
            "regulation": "applicable law",
            "action_needed": "what to add/change"
        }}
    ],
    "jurisdiction_notes": "jurisdiction considerations",
    "required_disclosures": ["mandatory disclosures"],
    "removed_clauses": ["clauses not applicable locally"],
    "added_clauses": ["clauses required locally"],
    "legal_review_recommendation": "need for local legal review"
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def market_brief(self) -> dict:
        if not self.target_market:
            return {"error": "Target market not set"}
        
        target_code, target_name, locale = self.target_market
        
        prompt = f"""Provide a localization market brief for {target_name}.

Return JSON:
{{
    "market": "{target_name}",
    "locale": "{locale}",
    "language_notes": {{
        "formality_levels": "formal vs informal usage",
        "honorifics": "titles and respect",
        "dialects": "regional variations"
    }},
    "cultural_dimensions": {{
        "individualism_collectivism": "cultural tendency",
        "power_distance": "hierarchy importance",
        "uncertainty_avoidance": "risk tolerance",
        "communication_style": "direct vs indirect"
    }},
    "business_culture": {{
        "meeting_etiquette": "meeting norms",
        "negotiation_style": "negotiation approach",
        "relationship_importance": "relationship vs transaction"
    }},
    "consumer_behavior": {{
        "purchase_drivers": ["what drives purchases"],
        "brand_preferences": "local vs international",
        "digital_behavior": "online habits"
    }},
    "holidays_events": ["key dates to consider"],
    "taboos": ["things to avoid"],
    "success_factors": ["keys to market success"]
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def quality_check(self, original: str, localized: str) -> dict:
        if not self.target_market:
            return {"error": "Target market not set"}
        
        target_code, target_name, locale = self.target_market
        
        prompt = f"""Quality check this localization for {target_name}.

Original:
{original}

Localized:
{localized}

Return JSON:
{{
    "quality_score": 85,
    "accuracy": {{
        "score": 90,
        "issues": ["accuracy issues"]
    }},
    "fluency": {{
        "score": 85,
        "issues": ["fluency issues"]
    }},
    "cultural_appropriateness": {{
        "score": 80,
        "issues": ["cultural issues"]
    }},
    "terminology": {{
        "score": 90,
        "inconsistencies": ["term issues"]
    }},
    "formatting": {{
        "score": 95,
        "issues": ["format issues"]
    }},
    "errors": [
        {{
            "type": "error type",
            "location": "where",
            "original": "original text",
            "current": "current translation",
            "suggestion": "correction"
        }}
    ],
    "overall_verdict": "approved/needs_revision/reject",
    "priority_fixes": ["most important fixes"]
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def _parse_json(self, content: str) -> dict:
        try:
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(content[start:end])
        except:
            pass
        return {"raw_response": content}


def display_menu():
    table = Table(title="🌍 Multilingual Content Localizer", show_header=True)
    table.add_column("Option", style="cyan", width=6)
    table.add_column("Feature", style="green")
    table.add_column("Description", style="white")
    
    table.add_row("1", "Localize Content", "Full content localization")
    table.add_row("2", "Cultural Analysis", "Check cultural appropriateness")
    table.add_row("3", "Adapt Marketing", "Marketing campaign adaptation")
    table.add_row("4", "Localize UI", "UI string localization")
    table.add_row("5", "Transcreate Slogan", "Creative slogan adaptation")
    table.add_row("6", "Legal Localization", "Legal content adaptation")
    table.add_row("7", "Market Brief", "Get market insights")
    table.add_row("8", "Quality Check", "Check localization quality")
    table.add_row("9", "Set Target Market", "Choose target market")
    table.add_row("0", "Exit", "Close application")
    
    console.print(table)


def main():
    console.print(Panel.fit(
        "[bold blue]🌍 Multilingual Content Localizer[/bold blue]\n"
        "[green]AI-Powered Cultural & Linguistic Adaptation[/green]\n"
        "[dim]Author: Pranay M[/dim]",
        border_style="blue"
    ))
    
    localizer = ContentLocalizer()
    
    while True:
        display_menu()
        if localizer.target_market:
            console.print(f"[dim]Target: {localizer.target_market[1]} ({localizer.target_market[2]})[/dim]")
        
        choice = Prompt.ask("\n[cyan]Select option[/cyan]", default="0")
        
        if choice == "0":
            console.print("[yellow]Goodbye! Go global! 🌍[/yellow]")
            break
        
        elif choice == "9":
            console.print("\n[bold]Available Markets:[/bold]")
            for mid, (code, name, locale) in MARKETS.items():
                console.print(f"  {mid}: {name} ({locale})")
            market_id = IntPrompt.ask("Select target market", default=1)
            if localizer.set_target_market(market_id):
                console.print(f"[green]✓ Target set to {localizer.target_market[1]}[/green]")
            continue
        
        if not localizer.target_market and choice != "9":
            console.print("[yellow]Please set target market first (option 9)[/yellow]")
            continue
        
        with console.status("[bold green]Localizing..."):
            if choice == "1":
                console.print("[dim]Paste content (end with 'EOF'):[/dim]")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "EOF":
                        break
                    lines.append(line)
                content_type = Prompt.ask("Content type", choices=CONTENT_TYPES, default="marketing")
                result = localizer.localize_content("\n".join(lines), content_type)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🌐 Localized Content"))
            
            elif choice == "2":
                console.print("[dim]Paste content (end with 'EOF'):[/dim]")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "EOF":
                        break
                    lines.append(line)
                result = localizer.cultural_analysis("\n".join(lines))
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🎭 Cultural Analysis"))
            
            elif choice == "3":
                console.print("[dim]Paste marketing campaign (end with 'EOF'):[/dim]")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "EOF":
                        break
                    lines.append(line)
                result = localizer.adapt_marketing("\n".join(lines))
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="📢 Marketing Adaptation"))
            
            elif choice == "4":
                console.print("Enter UI strings as key:value pairs (empty line to finish):")
                ui_strings = {}
                while True:
                    pair = input()
                    if not pair:
                        break
                    if ":" in pair:
                        key, value = pair.split(":", 1)
                        ui_strings[key.strip()] = value.strip()
                result = localizer.localize_ui(ui_strings)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="📱 UI Localization"))
            
            elif choice == "5":
                slogan = Prompt.ask("Enter slogan/tagline")
                result = localizer.transcreate_slogan(slogan)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="✨ Transcreation"))
            
            elif choice == "6":
                console.print("[dim]Paste legal text (end with 'EOF'):[/dim]")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "EOF":
                        break
                    lines.append(line)
                result = localizer.localize_legal("\n".join(lines))
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="⚖️ Legal Localization"))
            
            elif choice == "7":
                result = localizer.market_brief()
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="📊 Market Brief"))
            
            elif choice == "8":
                console.print("[dim]Paste original (end with 'EOF'):[/dim]")
                orig_lines = []
                while True:
                    line = input()
                    if line.strip() == "EOF":
                        break
                    orig_lines.append(line)
                console.print("[dim]Paste localized (end with 'EOF'):[/dim]")
                loc_lines = []
                while True:
                    line = input()
                    if line.strip() == "EOF":
                        break
                    loc_lines.append(line)
                result = localizer.quality_check("\n".join(orig_lines), "\n".join(loc_lines))
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="✅ Quality Check"))
        
        console.print("\n" + "="*50)


if __name__ == "__main__":
    main()
