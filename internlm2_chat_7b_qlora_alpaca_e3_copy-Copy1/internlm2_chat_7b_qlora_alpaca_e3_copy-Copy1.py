SYSTEM = 'xtuner.utils.SYSTEM_TEMPLATE.alpaca'
accumulative_counts = 16
alpaca_en = dict(
    dataset=dict(
        data_files=dict(
            train='Streamer-Sales/dataset/train_dataset/453_train copy.json'),
        path='json',
        type='datasets.load_dataset'),
    dataset_map_fn=None,
    max_length=2048,
    pack_to_max_length=True,
    remove_unused_columns=True,
    shuffle_before_pack=True,
    template_map_fn=dict(
        template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
        type='xtuner.dataset.map_fns.template_map_fn_factory'),
    tokenizer=dict(
        padding_side='right',
        pretrained_model_name_or_path=
        '/group_share/xtuner/xtuner/configs/internlm/internlm2_chat_7b',
        trust_remote_code=True,
        type='transformers.AutoTokenizer.from_pretrained'),
    type='xtuner.dataset.process_hf_dataset',
    use_varlen_attn=False)
alpaca_en_path = 'Streamer-Sales/dataset/train_dataset/453_train copy.json'
batch_size = 1
betas = (
    0.9,
    0.999,
)
custom_hooks = [
    dict(
        tokenizer=dict(
            padding_side='right',
            pretrained_model_name_or_path=
            '/group_share/xtuner/xtuner/configs/internlm/internlm2_chat_7b',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.engine.hooks.DatasetInfoHook'),
    dict(
        evaluation_inputs=[
            '请介绍一下你自己',
            'Please introduce yourself',
        ],
        every_n_iters=500,
        prompt_template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
        system='xtuner.utils.SYSTEM_TEMPLATE.alpaca',
        tokenizer=dict(
            padding_side='right',
            pretrained_model_name_or_path=
            '/group_share/xtuner/xtuner/configs/internlm/internlm2_chat_7b',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.engine.hooks.EvaluateChatHook'),
]
dataloader_num_workers = 0
default_hooks = dict(
    checkpoint=dict(
        by_epoch=False,
        interval=500,
        max_keep_ckpts=2,
        type='mmengine.hooks.CheckpointHook'),
    logger=dict(
        interval=10,
        log_metric_by_epoch=False,
        type='mmengine.hooks.LoggerHook'),
    param_scheduler=dict(type='mmengine.hooks.ParamSchedulerHook'),
    sampler_seed=dict(type='mmengine.hooks.DistSamplerSeedHook'),
    timer=dict(type='mmengine.hooks.IterTimerHook'))
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
evaluation_freq = 500
evaluation_inputs = [
    '请介绍一下你自己',
    'Please introduce yourself',
]
launcher = 'none'
load_from = None
log_level = 'INFO'
log_processor = dict(by_epoch=False)
lr = 0.0002
max_epochs = 3
max_length = 2048
max_norm = 1
model = dict(
    llm=dict(
        pretrained_model_name_or_path=
        '/group_share/xtuner/xtuner/configs/internlm/internlm2_chat_7b',
        quantization_config=dict(
            bnb_4bit_compute_dtype='torch.float16',
            bnb_4bit_quant_type='nf4',
            bnb_4bit_use_double_quant=True,
            llm_int8_has_fp16_weight=False,
            llm_int8_threshold=6.0,
            load_in_4bit=True,
            load_in_8bit=False,
            type='transformers.BitsAndBytesConfig'),
        torch_dtype='torch.float16',
        trust_remote_code=True,
        type='transformers.AutoModelForCausalLM.from_pretrained'),
    lora=dict(
        bias='none',
        lora_alpha=16,
        lora_dropout=0.1,
        r=64,
        task_type='CAUSAL_LM',
        type='peft.LoraConfig'),
    type='xtuner.model.SupervisedFinetune',
    use_varlen_attn=False)
optim_type = 'torch.optim.AdamW'
optim_wrapper = dict(
    accumulative_counts=16,
    clip_grad=dict(error_if_nonfinite=False, max_norm=1),
    dtype='float16',
    loss_scale='dynamic',
    optimizer=dict(
        betas=(
            0.9,
            0.999,
        ),
        lr=0.0002,
        type='torch.optim.AdamW',
        weight_decay=0),
    type='mmengine.optim.AmpOptimWrapper')
pack_to_max_length = True
param_scheduler = [
    dict(
        begin=0,
        by_epoch=True,
        convert_to_iter_based=True,
        end=0.09,
        start_factor=1e-05,
        type='mmengine.optim.LinearLR'),
    dict(
        begin=0.09,
        by_epoch=True,
        convert_to_iter_based=True,
        end=3,
        eta_min=0.0,
        type='mmengine.optim.CosineAnnealingLR'),
]
pretrained_model_name_or_path = '/group_share/xtuner/xtuner/configs/internlm/internlm2_chat_7b'
prompt_template = 'xtuner.utils.PROMPT_TEMPLATE.internlm2_chat'
randomness = dict(deterministic=False, seed=None)
resume = False
sampler = 'mmengine.dataset.DefaultSampler'
save_steps = 500
save_total_limit = 2
sequence_parallel_size = 1
tokenizer = dict(
    padding_side='right',
    pretrained_model_name_or_path=
    '/group_share/xtuner/xtuner/configs/internlm/internlm2_chat_7b',
    trust_remote_code=True,
    type='transformers.AutoTokenizer.from_pretrained')
train_cfg = dict(max_epochs=3, type='xtuner.engine.runner.TrainLoop')
train_dataloader = dict(
    batch_size=1,
    collate_fn=dict(
        type='xtuner.dataset.collate_fns.default_collate_fn',
        use_varlen_attn=False),
    dataset=dict(
        dataset=dict(
            data_files=dict(
                train='Streamer-Sales/dataset/train_dataset/453_train copy.json'),
            path='json',
            type='datasets.load_dataset'),
        dataset_map_fn=None,
        max_length=2048,
        pack_to_max_length=True,
        remove_unused_columns=True,
        shuffle_before_pack=True,
        template_map_fn=dict(
            template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
            type='xtuner.dataset.map_fns.template_map_fn_factory'),
        tokenizer=dict(
            padding_side='right',
            pretrained_model_name_or_path=
            '/group_share/xtuner/xtuner/configs/internlm/internlm2_chat_7b',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.dataset.process_hf_dataset',
        use_varlen_attn=False),
    num_workers=0,
    sampler=dict(shuffle=True, type='mmengine.dataset.DefaultSampler'))
use_varlen_attn = False
visualizer = None
warmup_ratio = 0.03
weight_decay = 0
work_dir = './work_dirs/internlm2_chat_7b_qlora_alpaca_e3_copy-Copy1'
