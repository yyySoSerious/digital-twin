"""Visual theme and styling configuration for the Digital Twin application."""

EXAMPLES = [
    "Tell me about your professional background.",
    "What are your main technical strengths?",
    "What certifications do you hold?",
    "How can I contact you?",
]

CSS = """
:root {
    color-scheme: dark;
}

html, body, gradio-app {
    background: #09121d !important;
}

.gradio-container {
    --body-text-color: #e4edf3;
    --body-text-color-subdued: #94a8b8;
    --block-background-fill: transparent;
    --block-border-color: transparent;
    --border-color-primary: #294254;
    --background-fill-primary: #0d1b28;
    --background-fill-secondary: #122433;
    --body-background-fill: #09121d;
    --color-accent: #65d6ca;
    --link-text-color: #8de1d6;
    width: 100% !important;
    max-width: 860px !important;
    min-width: 0 !important;
    margin: 0 auto !important;
    padding: 32px 28px 28px !important;
    background: transparent !important;
    color: #e4edf3 !important;
    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}

.gradio-container .main,
.gradio-container .contain {
    max-width: 100% !important;
}

.gradio-container .main {
    padding: 0 !important;
}

footer {
    display: none !important;
}

.gradio-container h1 {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 0 !important;
    color: #f0f7f8 !important;
    font-size: 24px !important;
    font-weight: 650 !important;
    letter-spacing: -0.035em;
    text-align: left !important;
}

.gradio-container h1::before {
    content: "OA";
    display: grid;
    place-items: center;
    width: 40px;
    height: 40px;
    border: 1px solid #37746f;
    border-radius: 12px;
    background: #12302f;
    color: #81ded2;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.02em;
}

.gradio-container [data-testid="markdown"] p {
    margin: 0 0 12px 52px;
    color: #91a7b6;
    font-size: 14px;
    line-height: 1.5;
}

#twin-chat {
    overflow: hidden !important;
    border: 1px solid #253e50 !important;
    border-radius: 18px !important;
    background: #0c1926 !important;
    box-shadow: 0 18px 50px #030a1280 !important;
}

#twin-chat .wrapper,
#twin-chat .bubble-wrap {
    background: transparent !important;
}

#twin-chat .bubble-wrap {
    padding: 24px !important;
}

#twin-chat .placeholder-content {
    max-width: 620px;
    margin: auto;
}

#twin-chat .welcome-mark {
    display: grid;
    place-items: center;
    width: 48px;
    height: 48px;
    margin: 0 auto 18px;
    border: 1px solid #34716d;
    border-radius: 16px;
    background: #143331;
    color: #8be4d7;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.06em;
}

#twin-chat .welcome-title {
    color: #eff8f8;
    font-size: 24px;
    font-weight: 650;
    letter-spacing: -0.035em;
    text-align: center;
}

#twin-chat .welcome-copy {
    margin-top: 8px;
    color: #94a8b8;
    font-size: 14px;
    line-height: 1.5;
    text-align: center;
}

#twin-chat .examples {
    gap: 10px !important;
    margin-top: 26px !important;
    padding: 0 !important;
}

#twin-chat button.example {
    min-height: 52px !important;
    padding: 12px 15px !important;
    border: 1px solid #294455 !important;
    border-radius: 11px !important;
    background: #112331 !important;
    color: #d3e2e8 !important;
    font: inherit !important;
    font-size: 13px !important;
    text-align: left !important;
    transition: background 150ms ease, border-color 150ms ease;
}

#twin-chat button.example:hover {
    border-color: #569e98 !important;
    background: #173433 !important;
}

#twin-chat .message-row .role > .message {
    padding: 10px 14px !important;
    border: 1px solid #294657 !important;
    border-radius: 14px !important;
    background: #122636 !important;
    color: #e4edf3 !important;
    font-size: 14px !important;
    line-height: 1.65 !important;
}

#twin-chat .user-row .role > .message {
    border-color: #376a69 !important;
    background: #173735 !important;
}

#twin-chat .message-row .message .message {
    border: 0 !important;
    background: transparent !important;
}

#twin-chat .message a {
    color: #8de1d6 !important;
}

.gradio-container .gr-group,
.gradio-container .gr-group .styler,
.gradio-container .form {
    background: transparent !important;
}

.gradio-container .gr-group {
    border: 0 !important;
}

#twin-input {
    margin-top: 12px !important;
    padding: 0 !important;
    border: 1px solid #365367 !important;
    border-radius: 14px !important;
    background: #0e1e2b !important;
    box-shadow: none !important;
}

#twin-input:focus-within {
    border-color: #65c7bb !important;
    box-shadow: 0 0 0 3px #65c7bb24 !important;
}

#twin-input .input-container {
    align-items: center;
    padding: 7px 8px 7px 16px;
    background: transparent !important;
}

#twin-input textarea {
    min-height: 42px !important;
    padding: 10px 0 !important;
    border: 0 !important;
    background: transparent !important;
    color: #e4edf3 !important;
    box-shadow: none !important;
    font: inherit !important;
    font-size: 14px !important;
}

#twin-input textarea::placeholder {
    color: #8197a7 !important;
}

#twin-input button {
    width: auto !important;
    height: 42px !important;
    min-width: 58px !important;
    padding: 0 14px !important;
    border: 0 !important;
    border-radius: 10px !important;
    background: #69d6c7 !important;
    color: #0a2423 !important;
    font-weight: 650 !important;
}

#twin-input button:hover {
    background: #8ae8da !important;
}

@media (max-width: 600px) {
    .gradio-container h1 {
        font-size: 21px !important;
    }

    #twin-chat .bubble-wrap {
        padding: 16px !important;
    }

    #twin-chat .welcome-title {
        font-size: 21px;
    }
}
"""

JS = """
() => {
    document.title = "Digital Twin";

    const focusChatInput = () => {
        const input = document.querySelector("#twin-input textarea");
        if (input) input.focus({ preventScroll: true });
    };

    setTimeout(focusChatInput, 300);

    const observeInput = (element) => {
        if (element.dataset.digitalTwinObserved) return;
        element.dataset.digitalTwinObserved = "true";

        let previouslyDisabled = element.disabled || element.readOnly;
        const observer = new MutationObserver(() => {
            const currentlyDisabled = element.disabled || element.readOnly;
            if (previouslyDisabled && !currentlyDisabled) {
                element.focus({ preventScroll: true });
            }
            previouslyDisabled = currentlyDisabled;
        });
        observer.observe(element, {
            attributes: true,
            attributeFilter: ["disabled", "readonly"]
        });
    };

    const initializeInput = () => {
        const input = document.querySelector("#twin-input textarea");
        if (input) observeInput(input);
    };

    setTimeout(initializeInput, 500);
    new MutationObserver(initializeInput).observe(document.body, {
        childList: true,
        subtree: true
    });
}
"""
